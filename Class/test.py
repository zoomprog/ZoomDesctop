import configparser

from pymongo import database
from pymongo.mongo_client import MongoClient
import pymongo
import database
from database.BDConfig import uri


client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.AppWise
coll = db.LoggedIn

