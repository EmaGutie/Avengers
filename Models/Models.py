from Models.db import db

class user(db.model):
    __tablename__="productos"
    id=  db.column(db.Integer, Primary_Key=True)
    nombre= db.column(db.String(100), nullable=False)
    alias=db.column(db.String,nullable=False)
    hablidades=db.column(db.String,foreignkey=True)
    actor=db.Column(db.String,nullable=False)
    def __init__(self,nombre,alias,hablidades,actor):
        self.id
        self.nombre = nombre
        self.alias = alias
        self.habilidades = hablidades
        self.actor = actor
    def to_dict(self):
        return{
            'id' :self. id,
            'nombre':self. nombre,
            'alias' :self. alias,
            'habilidades' :self. habilidades,
            'actor' :self. actor
            
            
        }
