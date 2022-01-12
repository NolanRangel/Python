from flask import Flask, render_template, request, redirect

from user import User

app=Flask(__name__)
app.secret_key = 'something'

@app.route('/')
def index():
    return render_template('new_user.html')


@app.route('/user/new')
def new():
    return render_template("user.html")


@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.create(request.form)
    return redirect('/users')


@app.route('/users')
def users():
    users=User.get_all()
    return render_template("users.html",users=users)


@app.route('/user/edit/<int:id>')
def edit(id):    #get_one
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):   #get_one
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user=User.get_one(data))


@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return render_template('users.html')

if __name__=="__main__":
    app.run(debug=True)