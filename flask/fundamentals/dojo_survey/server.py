from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'Caliber'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/survey', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    # print(request.form)
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/redirect')

@app.route('/redirect')
def show():
    return render_template('redirect.html')



if __name__ == "__main__":
    app.run(debug=True)