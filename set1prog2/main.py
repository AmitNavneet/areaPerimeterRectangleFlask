from flask import Flask,request
from flask import render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate")
def calculate():
    length=float(request.args['length'])
    breadth=float(request.args['breadth'])

    area=length*breadth
    
    peri=2*(length+breadth)
    str= f"<h1 style='color:red';>"
    str=str+f"Length={length}<br>"
    str=str+f"Breadth={breadth}<br>"
    str=str+f"Area={area}<br>"
    str=str+f"perimeter={peri}</h1>"

    return str

if __name__=="__main__":
    app.run(debug=True)