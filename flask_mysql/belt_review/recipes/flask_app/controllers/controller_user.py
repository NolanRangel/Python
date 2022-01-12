# controller
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)


@app.route('/')
def index():
    # user = User.user_get_all()
    return render_template('index.html',)


@app.route('/user/register', methods=['POST'])
def user_create():

        if not User.validate_registration(request.form):
            return redirect('/')
        # get email from you form data
        email = request.form["email"]
        email = {
            **request.form,
            'email': email
        }

        # check if someone already register with the email
        user = User.get_one_by_email(email)
        # print(user)
        # print('*******')
        if not user:
            # the email doesnt exist
            pass
        else:
            flash('email already exists', 'err_email')
            return redirect('/')

        hash_pw = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,
            'password': hash_pw
        }
        id = User.user_create(data)
        # print('**')
        # print(id)

        session['first_name'] = data['first_name']
        session['id'] = id
        # session['email'] = data['email']

        return redirect('/user')


@app.route('/user/login', methods=['POST'])
def user_login():

        if not User.validate_login(request.form):
            print(request.form)
            return redirect('/')

        potential_user = User.get_one_by_email({'email': request.form['email']})

        if not potential_user or not bcrypt.check_password_hash(potential_user.password, request.form['password']):
            flash("Incorrect password", "err_login_password")
            return redirect('/')

        session['id'] = potential_user.id
        session['first_name'] = potential_user.first_name

        return redirect('/user')


@app.route('/logout')
def logout():
    if not session.get('id'):
        return render_template('index.html')
    else:
        del session['first_name']
        del session['id']
        return redirect('/')
    # del session['email']


# show
@app.route('/user')
def recipe_users():
    if not session.get('id'):
        return render_template('index.html')
    else:
        data = {
            'id': session['id']
        }
        print(data)
        user = User.user_get_one(data)
        print(user)
        print(session['id'])
        print('!!!!!!')
        return render_template("dashboard.html", user=user)


# @app.route('/success')
# def user_success():
#     if not session.get('first_name'):
#         return render_template('index.html')
#     else:
#         return render_template('success.html')

    # if not session['id']:
    #     return redirect('/')
    # else:
