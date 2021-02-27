from logging import debug
from flask import Flask,request
from tinydb import TinyDB,Query
import json


app=Flask(__name__)


q=Query()

file=open("country_by_capital_city.json").read()

f=json.loads(file)

db=TinyDB("database.json")

table1=db.table("inform country and city")

table1.truncate()
table1.insert_multiple(f)

@app.route("/api",methods=["POST","GET"])
def api():
    if request.method=="POST":
        r=request.form
        country=r.get("country","")
        country=country.capitalize()
        # print(r)


        return "ok"
    
    return "ok"




def database(country:str)->dict:
    pass



app.run(debug=True)




