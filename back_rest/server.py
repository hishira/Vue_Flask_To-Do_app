from flask import Flask, escape, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId
import os
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ToDoApp"
mongo = PyMongo(app)
CORS(app)

@app.route('/', methods=['GET'])
def getTasks():
    try:
        tasks = mongo.db.Task
        result = []
        for i in tasks.find():
            result.append({"_id":str(i['_id']),"tresc_zadania":i['tresc_zadania']})
        response =  jsonify(result) 
        return response
    except Exception as e:
        return (str(e))

def getTasksHelper(tasks):
    return jsonify([{"_id":str(i['_id']),"tresc_zadania":i['tresc_zadania']} for i in tasks])

@app.route('/removeTask/<id>', methods=['POST'])
def removeTask(id):
    try:
        tasks = mongo.db.Task
        x = tasks.delete_one({"_id":ObjectId(id)})
        return getTasksHelper(tasks.find())
    except Exception as e:
        return (str(e))


@app.route('/addTask', methods=['POST'])
def addTask():
    try:
        requestString = request.data.decode('UTF-8')
        requestString = requestString.replace('"','')
        print(requestString)
        tasks = mongo.db.Task
        tasks.insert({'tresc_zadania':requestString})
        return "Add task"
    except Exception as e:
        return (str(e))

@app.route('/update/<id>', methods=['POST'])
def update(id):
    try:
        requestString = request.data.decode('UTF-8')
        tasks = mongo.db.Task
        x = tasks.update_one({"_id":ObjectId(id)},{"$set":{'tresc_zadania':requestString}})
        return  getTasksHelper(tasks.find())
    except Exception as e:
        return (str(e))
