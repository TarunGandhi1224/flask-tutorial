from flask import Flask,request,jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import pymongo
load_dotenv()
mongo_uri=os.getenv('mongo_uri')

client=pymongo.MongoClient(mongo_uri)
db=client.test
collection=db['Flask_tutorial']
app= Flask(__name__)
@app.route('/submit',methods=['POST']) #1234_temp
def submit():
    form_data=dict(request.json)
    collection.insert_one(form_data)
    return 'Data Subitted Successfully'
@app.route('/admin')
def admin():
    data=collection.find()
    data=list(data)
    for item in data:
        print(item)
        del item['_id']
        data={
            'data':data
        }
    return jsonify(data)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)