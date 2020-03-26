from flask import Flask,escape,request, json
import database_connect


app = Flask(__name__)

@app.route('/',methods=['GET'])
def getTasks():
    database_connect.makeConnection()
    records = database_connect.makeQuerry('select * from zadania')
    response =  json.jsonify(records)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/removeTask/<id>',methods=['POST'])
def removeTask(id):
	database_connect.removeTask("delete from zadania where zadanie_id='"+id+"'")
	records = database_connect.makeQuerry('select * from zadania')
	response = json.jsonify(records)
	response.headers.add('Access-Control-Allow-Origin',"*")
	return response

@app.route('/addTask',methods=['POST'])
def addTask():
	requestString = request.data.decode('UTF-8')
	database_connect.addTask("""insert into zadania(tresc_zadania) values ('"""+requestString+"""')""")
	records = database_connect.makeQuerry('select * from zadania')
	response = json.jsonify(records)
	response.headers.add('Access-Control-Allow-Origin',"*")
	return response