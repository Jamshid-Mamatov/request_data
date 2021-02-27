from flask import Flask,request

app=Flask(__name__)

@app.route("/form",methods=["GET","POST"])

def get_form():

    if request.method=="POST":
        r=request.form
        print(r)
        a=r.get("a",0)
        b=r.get("b",0)
        return {"sum":a+b}


    return "ok"

app.run(debug=True)