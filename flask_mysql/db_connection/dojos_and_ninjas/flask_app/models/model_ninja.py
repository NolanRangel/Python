from typing import Dict
from flask_app.config.mysqlconnection import connectToMySQL


DATABASE = 'dojos_and_ninjas'


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.dojo_id = data['dojo_id']

    
# *************************************************************************CREATE
    @classmethod
    def ninja_create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s, NOW(), NOW(), %(dojo_id)s );"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # comes back as the new row id
        return result


# **************************************************************************RETRIEVE
    @classmethod
    def ninja_get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    
    # @classmethod
    # def get_all_ninjas(cls, data:dict):
    #     query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     dojos = []
    #     for dojo in results:
    #         dojos.append( cls(dojo) )
    #     return dojos


    @classmethod
    def ninja_get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])


# ***************************************************************************UPDATE
    @classmethod
    def ninja_update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


# ***************************************************************************DESTROY
    @classmethod
    def ninja_destroy(cls,data):
        print(data)
        print('*******')
        query  = "DELETE FROM ninjas WHERE ninjas.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)