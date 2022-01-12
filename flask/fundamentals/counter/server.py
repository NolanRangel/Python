from flask import Flask, render_template, request, redirect,session,url_for


app = Flask(__name__)
app.secret_key = 'Caliber'

# our index route will handle rendering our form
@app.route('/')
def count():
    if 'visits'  in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
        
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.pop('visits')
    return redirect('/')


@app.route('/add_two')
def add_two():
    session['visits'] += 1
    return redirect('/')

# @app.route('/user_add', methods=['POST'])
# def user_increment():
#     # print(request.form)
#     increment = request.form['user_input']
#     print(increment)
#     session['count'] += int(increment)-1
#     session['visits'] -= 1
#     return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)