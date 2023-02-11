import pymongo
from Classes import Estudiantes, DbMongo

def main():
    
    db = DbMongo.getDB()
    collection = db['Estudiantes']
    
    estudiante = Estudiantes("Maria", "Ocon", "***-***", "****@***")
   
    #SU FUNCION ES GUARDAR Y ENVIAR AL MONGODB
    estudiante.save(db) 
    
    estudiante.update() 
    
    ## print(estudiante.__dict__)
    
    ## collection.insert_one(estudiante.__dict__)

if __name__ == '__main__':
    main()

#CAPTURA DE DATOS
## collection.insert_one({ "Nombre" : " Kevin"})

## for document in collection.find():
    ## print(document)