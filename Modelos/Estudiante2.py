from app import db

class estudiante2(db.Model):
    __tablename__="Estudiante"

    id=db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String())
    nombre = db.Column(db.String())
    apellido = db.Column(db.String)

    def __init__(self, Cedula, Nombre, Apellido):
        self.cedula = Cedula
        self.nombre = Nombre
        self.apellido = Apellido

    def __repr__(self):
        return f"Cedula:{self.cedula}, Nombre:{self.nombre}, Apellido:{self.apellido}"