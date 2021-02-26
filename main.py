from flask import Flask,request

app=Flask(__name__)

@app.route("/")

def request_inform():
    
    path=request.path
    full_path=request.full_path
    script_root=request.script_root
    base_url=request.base_url
    url=request.url

    inform=f"""
    <p>path:{path}</p>
    <p>full_path:{full_path}</p>
    <p>script_root:{script_root}</p>
    <p>base_url:{base_url}</p>
    <p>url:{url}</p>

    """

    return inform

app.run(debug=True)