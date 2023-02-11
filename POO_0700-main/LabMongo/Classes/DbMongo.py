
import pymongo

class DbMongo:
    
    #@staticmethod = DECORADOR => QUE TIPO DE ESTRUCTURA VA A TENER EL SIGUIENTE METODO QUE SE VA A DEFINIR 
    
    @staticmethod
    def getDB():
        user = "KVJ"
        password = "Rinnegan2)_("
        cluster = "cluster.h25bvf7.mongodb.net"
        query_string = "retryWrites=true&w=majority"

        ## CONNECTION STRING
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
        user 
        , password
        , cluster 
        , query_string
        )

        client = pymongo.MongoClient(uri) 
        db = client['UNAH']
        
        #SU FUNCION ES RETORNAR EN LA DB LO CUAL ENVIA AL APP.pY
        return db
    
    
    