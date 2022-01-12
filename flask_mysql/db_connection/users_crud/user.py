from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

# *******************************************CREATE

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        # comes back as the new row id
        result = connectToMySQL('user_schema').query_db(query,data)
        return result
    
# *******************************************RETRIEVE
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_schema').query_db(query)
        # comes back as a list of dictionaries
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE user_id = %(id)s";
        result = connectToMySQL('user_schema').query_db(query,data)
        return cls(result[0])
    
# *******************************************UPDATE

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE user_id = %(id)s;"
        return connectToMySQL('user_schema').query_db(query,data)
        # returns nothing

# *******************************************DESTROY

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE user_id = %(id)s;"
        return connectToMySQL('user_schema').query_db(query,data)
        # returns nothing
        
        


