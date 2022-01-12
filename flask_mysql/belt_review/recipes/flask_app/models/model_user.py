from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re

from flask_app.models.model_recipe import Recipe


DATABASE = 'recipes_db'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

        self.recipes = []

    def __repr__(self) -> str:      # returns a string representation of the object
        return f"user object id = {self.id}"


    def fullname(self):
        return f"{self.first_name} {self.last_name}"



# *************************************************************************CREATE
    @classmethod
    def user_create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, updated_at, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        # comes back as the new row id
        return connectToMySQL(DATABASE).query_db(query, data)


# **************************************************************************RETRIEVE


    @classmethod
    def user_get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    
    @classmethod
    def get_one_by_email(cls,data:dict):
        print('*******')
        print(data)
        print('*******')
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print('**********')
        print(results)
        print('**********')
        if results:
            return cls(results[0])
        # return False


            
    @classmethod        
    def user_get_one(cls,data:dict):
        query  = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id";
        results = connectToMySQL(DATABASE).query_db(query,data)
        user = cls(results[0])

            
        for recipe in results:
            print('*************************')
            print(data)
            print('******************************')
            data = {
                'id': recipe['recipes.id'],
                'name': recipe['name'],
                'description': recipe['description'],
                'instructions': recipe['instructions'],
                'make_time': recipe['make_time'],
                'created_at': recipe['recipes.created_at'],
                'updated_at': recipe['recipes.updated_at'],
                'user_id': recipe['user_id'],
            }
            print('**********')
            recipe = Recipe(data)
            print(recipe)
            print('**********')
                    # print(result)
            user.recipes.append(recipe)
        return user

# ***************************************************************************UPDATE


    @classmethod
    def user_update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, password=%(password)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


# ***************************************************************************DESTROY


    @classmethod
    def user_destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
#**************************************************************************VALIDATE


    @staticmethod
    def validate_registration(data:dict): #returns bool
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
            flash("First Name must be more than 2 characters", "err_first_name")
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last Name must be more than 2 characters", "err_last_name")

        if len(data['email']) < 1:
            flash("Email is required", "err_email")
            is_valid = False
        # elif  EMAIL_REGEX.match(data["email"]):
        #     flash("Email already exists!", "err_email")
        #     is_valid = False
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email!", "err_email")
            is_valid = False

        if len(data['password']) < 8:
            is_valid = False
            flash("Invalid password, please check password requirments", "err_password")
        elif not PASSWORD_REGEX.match(data["password"]):
            flash("Password must contain 8 characters, one number and one special character", "err_password")
            is_valid = False
            
        if len(data['confirm_password']) != len(data['password']):
            is_valid = False
            flash("Passwords do not match", "err_confirm_password")

        return is_valid
    
    @staticmethod
    def validate_login(data:dict):  #returns bool
        is_valid = True
        
        if len(data['email']) < 1:
            is_valid = False
            flash("Email is required", "err_login_email")
        elif not EMAIL_REGEX.match(data["email"]):
            is_valid = False
            flash("Invalid email address!", "err_login_email")
        if len(data['password']) < 1:
            is_valid = False
            flash("Password is required", "err_login_password")
        elif not PASSWORD_REGEX.match(data["password"]):
            flash("Password must contain 8 characters, one number and oner special character", "err_login_password")
            is_valid = False
        
        print(is_valid)    
        return is_valid
