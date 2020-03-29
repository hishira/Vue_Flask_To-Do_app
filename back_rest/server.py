from flask import Flask,escape,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS,cross_origin

import database_connect
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Task

@app.route('/',methods=['GET'])
def getTasks():
    try:
    	tasks = Task.query.all()
    	response = jsonify([e.serialize() for e in tasks])
    	return response
    except Exception as e:
    	return (str(e))

@app.route('/removeTask/<id>',methods=['POST'])
def removeTask(id):
	try:
		Task.query.filter_by(zadanie_id=id).delete()
		db.session.commit()
		tasks = Task.query.all()
		response = jsonify([e.serialize() for e in tasks])
		return response
	except Exception as e:
		return (str(e))

@app.route('/addTask',methods=['POST'])
def addTask():
	try:
		requestString = request.data.decode('UTF-8')
		task = Task(tresc_zadania=requestString)
		db.session.add(task)
		db.session.commit()
		return "Add task"
	except Exception as e:
		return (str(e))

@app.route('/update/<id>',methods=['POST'])
def update(id):
	try:
		requestString = request.data.decode('UTF-8')
		task = Task.query.filter_by(zadanie_id=id).first()
		task.tresc_zadania = requestString
		db.session().commit()
		return "Update task"
	except Exception as e:
		return (str(e))
