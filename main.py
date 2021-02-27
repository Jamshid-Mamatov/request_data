from flask import Flask,request

app=Flask(__name__)

@app.route("/form")

def get_form():

    r=request.values

    print(r)

    return "ok"

app.run(debug=True)