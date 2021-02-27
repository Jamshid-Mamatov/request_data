from flask import Flask,request

app=Flask(__name__)

@app.route("/")

def api():
    r=request.args
    print(r)
    print(request.url)

    return "ok"

app.run(debug=True)