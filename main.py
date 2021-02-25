from flask import Flask,request

app = Flask(__name__)


@app.route('/api')
def api():
    r = request.args
    a=r['a']
    b=r['b']
    return {'a':a,'b':b}


app.run(debug=True)