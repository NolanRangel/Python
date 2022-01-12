# controller
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja




@app.route('/')
def index():
    dojos = Dojo.dojo_get_all()
    return render_template('index.html', dojos=dojos)


@app.route('/dojo/create',methods=['POST'])
def create():
    Dojo.dojo_create(request.form)
    return redirect('/')


@app.route('/dojo/show/<int:id>')
def show(id):
    data ={
        'id': id
    }   
    dojo = Dojo.dojo_get_one(data)
    # print(dojo)
    # print('*********')
    return render_template("dojo_ninjas.html",dojo=dojo )


@app.route('/users')
def users():
    dojos=Dojo.dojo_get_all()
    return render_template("dojo_ninjas.html",dojos=dojos)


@app.route('/user/edit/<int:id>')
def edit(id):    #get_one
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=Dojo.get_one(data))




@app.route('/user/update',methods=['POST'])
def update():
    Dojo.dojo_update(request.form)
    return redirect('/users')

@app.route('/destroy/<int:id>/dojo')
def destroy(id):
    data ={
        'id': id
    }
    Dojo.dojo_destroy(data)
    return redirect('/')