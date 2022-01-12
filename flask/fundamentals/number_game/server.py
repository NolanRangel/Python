from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Caliber'

@app.route('/')
def index():
    session['number'] = random.randint(1,100)
    print(session['number'])
    return render_template("index.html")

@app.route('/form_submit', methods=['POST'])
def check_number():
    if 'visits'  in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    print(type(request.form['form_number']))
    if int(request.form['form_number']) == session['number']:
        return redirect('/correct.html')
    else: 
        return redirect('/wrong.html')
    
    
@app.route('/wrong.html')
def wrong_number():
    if int(session['visits']) == 5:
        return render_template('lose.html')
    else:
        return render_template('wrong.html')


@app.route('/correct.html')
def correct_number():
    session.pop('visits')
    return render_template('correct.html')
    
        



if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)

    return render_template("index.html")

@app.route('/guess',methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')