from flask import Flask, escape, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
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
        print(result)
        response =  jsonify(result) 
        print(response)
        return response
    except Exception as e:
        return (str(e))

'''
@app.route('/removeTask/<id>', methods=['POST'])
def removeTask(id):
    try:
        Task.query.filter_by(zadanie_id=id).delete()
        db.session.commit()
        tasks = Task.query.all()
        response = jsonify([e.serialize() for e in tasks])
        return response
    except Exception as e:
        return (str(e))


@app.route('/addTask', methods=['POST'])
def addTask():
    try:
        requestString = request.data.decode('UTF-8')
        task = Task(tresc_zadania=requestString)
        db.session.add(task)
        db.session.commit()
        return "Add task"
    except Exception as e:
        return (str(e))


@app.route('/update/<id>', methods=['POST'])
def update(id):
    try:
        requestString = request.data.decode('UTF-8')
        task = Task.query.filter_by(zadanie_id=id).first()
        task.tresc_zadania = requestString
        db.session().commit()
        return "Update task"
    except Exception as e:
        return (str(e))
'''