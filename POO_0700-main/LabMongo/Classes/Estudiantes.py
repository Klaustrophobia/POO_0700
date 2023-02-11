from Classes import DbMongo

class Estudiantes: 
      
    def __init__(self, nombre, apellido, numero, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.correo = correo
        self.__collection = "Estudiantes"
        
    ##AGREGAR UN METODO ESCRIBIR [QUE RECIBA DATOS QUE UNO INGRESA] Y LO MANDE AL MONGODB
    
    def Escribir(self):
        print("Ingrese Nombre:")
        nombre = input()
        print("Ingrese Apellido:")
        apellido = input()
        print("Ingrese numero:")
        numero = input()
        print("Ingrese correo:")
        correo = input()    
        
    def save(self, db):
        collection = db [self.__collection]
        collection.insert_one(self.__dict__)
    