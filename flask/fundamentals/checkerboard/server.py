from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def checkers():
    return render_template("index.html",numx=8,numy=8,colorx="red",colory="black")

@app.route('/<int:numy>')
def  checkers_y(numy):
    return render_template("index.html", numx=8,numy=numy,colorx="red",colory="black")

@app.route('/<int:numx>/<int:numy>')
def  checkers_x_y(numx,numy):
    return render_template("index.html", numx=numx,numy=numy,colorx="red",colory="black")

@app.route('/<int:numx>/<int:numy>/<string:colorx>/<string:colory>')
def  checkers_x_y_colors(numx,numy,colorx,colory):
    return render_template("index.html", numx=numx,numy=numy,colorx=colorx,colory=colory)





if __name__ == "__main__":
    app.run(debug=True)