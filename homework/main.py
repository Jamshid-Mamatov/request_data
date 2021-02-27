from logging import debug
from flask import Flask,request
from tinydb import TinyDB

app=Flask(__name__)


@app.route("/api",methods=["POST","GET"])
def api():
    if request.method=="POST":
        r=request.form
        country=r.get("country","")
        country=country.capitalize()
        # print(r)


        return "ok"
    
    return "ok"


app.run(debug=True)


