from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_ninja import Ninja

DATABASE = 'dojos_and_ninjas'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.ninjas = []
        
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    # @property
    # def ninjas(self):
    #     return Ninja.get_all_ninjas({'dojo_id': self.id})
    
# *************************************************************************CREATE
    @classmethod
    def dojo_create(cls, data):          #create new dojo
        query = "INSERT INTO dojos (name, updated_at, created_at) VALUES (%(name)s, created_at=NOW(), updated_at=NOW());"
        # comes back as the new row id
        return connectToMySQL(DATABASE).query_db(query,data)
        


# **************************************************************************RETRIEVE
    @classmethod
    def dojo_get_one(cls,data:dict):
        query  = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;";
        results = connectToMySQL(DATABASE).query_db(query,data)
        result = cls(results[0])
        for ninja in results:
            # print('*************************')
            # print(data)
            # print('******************************')
            data = {
                'id': ninja['ninjas.id'],
                'first_name': ninja['first_name'],
                'last_name': ninja['last_name'],
                'age': ninja['age'],
                'created_at': ninja['ninjas.created_at'],
                'updated_at': ninja['ninjas.updated_at'],
                'dojo_id': ninja['dojo_id'],
            }
            # print('**********')
            # print(data)
            ninja = Ninja(data)
            # print('**********')
            # print(result)
            result.ninjas.append(ninja)
        return result


    @classmethod
    def dojo_get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos


# ***************************************************************************UPDATE
    @classmethod
    def dojo_update(cls,data):
        query = "UPDATE dojos SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


# ***************************************************************************DESTROY
    @classmethod
    def dojo_destroy(cls,data):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)