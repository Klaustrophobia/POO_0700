import pymongo
from Classes import DbMongo
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()