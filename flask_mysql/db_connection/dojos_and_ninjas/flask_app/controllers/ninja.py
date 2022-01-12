
# controller
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo






@app.route('/ninja/add')
def ninja_edit():    #get_one
    dojos = Dojo.dojo_get_all()
    print('***********')
    print(dojos)
    print('***********')
    # ninjas = Ninja.ninja_get_all()
    return render_template("new_ninja.html", dojos=dojos)


@app.route('/ninja/create',methods=['POST'])
def ninja_create():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.ninja_create(data)
    print('***')
    print(request.form)
    print('***')
    return redirect('/')


@app.route('/destroy/<int:id>/ninja')
def ninja_destroy(id):
    data ={
        'id': id
    }
    Ninja.ninja_destroy(data)
    return redirect('/')

