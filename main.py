from flask import Flask,request

app=Flask(__name__)

@app.route("/")

def api():

    r=request.args
    print(r)
    # print(request.url)
    a=int(r['a'])
    b=int(r['b'])

    return {"result":a+b}

app.run(debug=True)