# controller
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
from flask_bcrypt import Bcrypt  

bcrypt = Bcrypt(app)




# RESTful architecture

# /user/new
# /user/create
# /user/<int:id>
# user/edit/<int:id>
# user/update<int:id>/
# user/destroy<int:id>/





# NEW -- RENDERS TO CREATE

@app.route('/recipe/new')
def recipe_new():
    
    #lOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')
    
    #GRABS USER ID TO USE TO ADD RECIPE/ROUTES WITH GET TO CREATE
    else:   
        user=User.user_get_one({'id':session['id']})
        
        return render_template("recipe_new.html", user=user)


# CREATE -- REDIRECT TO DASHBOARD


@app.route('/recipe/create',methods=['POST'])
def recipe_create():
    
    #LOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')
    
    #FIELD VALIDATION/
    else:
        if not Recipe.validate_recipe(request.form):
            #REDIRECTS BACK TO SAME PAGE IF FIELDS INVALID/FIELDS NOT UPDATED
            return redirect(request.referrer)
        print(request.form)
        #DOUBLE LOGIN CHECK??
        if not session.get('id'):
            return render_template('index.html')
        #CONSTRUCTS RECIPE AND PASSES AS data
        else:
            data = {
            "name": request.form["name"],
            "description" : request.form["description"],
            "instructions" : request.form["instructions"],
            "make_time" : request.form["make_time"],
            "created_at" : request.form["created_at"],
            "user_id": session['id']
            }
            
            print('***')
            print(request.form)
            print('***')
            
            #CREATES NEW RECIPE
            Recipe.recipe_create(data)
            
            return redirect('/user')           # **would have to render session to transfer user data from create to show



# SHOW -- RENDERS TO SHOW


@app.route('/recipe/<int:id>')
def recipe_show(id):
    
    #LOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')
    
    else:
        data = {
            'id':id
        }
        #RETREIVS RECIPE
        recipe=Recipe.recipe_get_one(data)
        print(recipe)

        return render_template("recipe_show.html",recipe=recipe)
    
    
# EDIT -- RENDERS TO EDIT


@app.route('/recipe/edit/<int:id>')
def recipe_edit(id):   
    
    #LOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')
    
    else:
        data ={ 
            "id":id
        }
        #UPDATES RECIPE ON BUTON CLICK AND GRABS THE RECIPE ON PAGE LOAD
        Recipe.recipe_update(request.form)
        recipe=Recipe.recipe_get_one(data)
        
        print(recipe)
        
        return render_template("recipe_edit.html", recipe=recipe)



# UPDATE -- REDIRECTS TO DASHBOARD



@app.route('/recipe/update/<int:id>' ,methods=['POST'])
def recipe_update(id):
    
    #LOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')
    #FIELD VALIDATION
    else:
        if not Recipe.validate_recipe(request.form):
            return redirect(request.referrer)
        
        # print(request.form)
        
        data = {
            **request.form,
            'id': id
        }
    
        # print(request.form)
        
        #UPDATE RECIPE
        Recipe.recipe_update(data)
        
        return redirect('/user')


# DESTROY -- REDIRECTS TO DASHBOARD


@app.route('/recipe/destroy/<int:id>')
def recipe_destroy(id):
    
    #LOGIN CHECK
    if not session.get('id'):
        return render_template('index.html')
    
    else:
        data = {
            'id':id
        }
        
        # print(data)
        
        #DELETES RECIPE ROUTES BACK TO DASHBOARD
        Recipe.recipe_destroy(data)
        
        return redirect("/user")






