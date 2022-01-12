from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re


#MAKE SURE TO UPDATE

DATABASE = 'recipes_db'





class Recipe:      # update init to reflect table data
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.make_time = data['make_time']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

# *******************************************CREATE

    @classmethod        #update to reflect table data (returns a row id number)
    def recipe_create(cls, data:dict):
        query = "INSERT INTO recipes (name, description, instructions , make_time, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(make_time)s, %(created_at)s, NOW(),  %(user_id)s);"

        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
# *******************************************RETRIEVE
    
    @classmethod
    def recipe_get_all(cls):    # returns a list of dictionaries
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for u in results:
            recipes.append( cls(u) )
        return recipes

    @classmethod        # returns a list of a single dictionary
    def recipe_get_one(cls,data:dict):
        query  = "SELECT * FROM recipes WHERE id =%(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
# *******************************************UPDATE

    @classmethod
    def recipe_update(cls,data:dict):        # update to reflect table (returns nothing)
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s, make_time=%(make_time)s,created_at= %(created_at)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

# *******************************************DESTROY

    @classmethod
    def recipe_destroy(cls,data:dict):        # returns nothing
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    
#**********************************************VALIDATOR
    
    
    @staticmethod
    def validate_recipe(data:dict): #returns bool
        is_valid = True
        
        
        if len(data['name']) < 2:
            is_valid = False
            flash("Name must be more than 2 characters", "err_name")
            
        if len(data['description']) < 2:
            is_valid = False
            flash("Description must be more than 2 characters", "err_description")

        if len(data['instructions']) < 2:
            flash("Instructions must be more than 2 characters", "err_instructions")
            is_valid = False
        
        if len(data['created_at']) < 2:
            is_valid = False
            flash("Please enter a date", "err_created_at")
            
        return is_valid