from logging import debug
from flask import Flask,request

app=Flask(__name__)


@app.route("/api",methods=["POST"])
def api():
    if request.method=="POST":
        return {}
    return "ok"


app.run(debug=True)