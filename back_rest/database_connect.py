import psycopg2

obj = {}

def makeConnection():
    try:
        obj.update({"connection" : psycopg2.connect(user='michal',password='michal',host='localhost',database='michal')})
        obj.update({"cursor" : obj['connection'].cursor()})
    except:
        print("Blad")


def makeQuerry(querryString):
    if obj['connection']:
        obj['cursor'].execute(querryString)
        records = obj['cursor'].fetchall()
        obj['connection'].commit()
        return records
    else:
        return None

def removeTask(querryString):
    if obj['connection']:
        obj['cursor'].execute(querryString)
        obj['connection'].commit()
    else:
        return None

def addTask(querryString):
    print(obj.keys())
    if obj['connection']:
        obj['cursor'].execute(querryString)
        obj['connection'].commit()
    else:
        return None