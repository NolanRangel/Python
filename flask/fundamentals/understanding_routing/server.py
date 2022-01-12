from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:text>')
def repeat(num,text):
    return f"{text * num}"



if __name__ == '__main__':
    app.run(debug=True)
    