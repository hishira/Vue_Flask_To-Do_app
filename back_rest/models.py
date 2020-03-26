from server import db

class Task(db.Model):
    __tablename__ = 'tasks'
    zadanie_id = db.Column(db.Integer,primary_key=True)
    tresc_zadania = db.Column(db.String())
    def __init__(self,tresc_zadania):
        self.tresc_zadania = tresc_zadania

    def __repr__(self):
        return '<id {}>'.format(self.zadanie_id)
    
    def serialize(self):
        return {
            'zadanie_id':   self.zadanie_id,
            'tresc_zadania': self.tresc_zadania
        }

