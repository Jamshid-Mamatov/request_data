from flask import Flask,request

app=Flask(__name__)

@app.route("/")

def api():

    r=request.args
    print(r)
    # print(request.url)
    
    a=int(r.get("a",0))
    b=int(r.get("b",0))

    for k,v in r.items():
        print(k,v)
    return {"result":a+b}

app.run(debug=True)