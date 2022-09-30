from app import db
from Modelos import Estudiante2

# db.create_all()
'''
estudiante = Estudiante2.estudiante2("1237845","Alexander","Amaya")
estudiante_2= Estudiante2.estudiante2("1433456","Alejandro", "Valero")

db.session.add_all([estudiante,estudiante_2])
db.session.commit()
'''

'''Muestra todos los registros 
resultado = Estudiante2.estudiante2.query.all()
print("los estudiantes son:")
print(resultado)
'''
''' mostrar por parametro
resultado2 = Estudiante2.estudiante2.query.filter_by(nombre="Jersson")
print(resultado2.all())
'''
#mostrar por id
resultado3 = Estudiante2.estudiante2.query.get(4)
print(resultado3)

''' update
resultado4 = Estudiante2.estudiante2.query.get(3)
resultado4.nombre="Pedro1111"
resultado4.cedula="129839023"
db.session.add(resultado4)
db.session.commit()
print(resultado4)
'''
'''Eliminar registro'''
'''resul=Estudiante2.estudiante2.query.get(3)
db.session.delete(resul)
db.session.commit()'''
