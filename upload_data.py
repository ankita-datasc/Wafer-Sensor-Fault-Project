from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri=("mongodb+srv://ankitachandrakar2301:1vtfsJ0VvcotX2W0@cluster0.o0z19.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="INVENTORY"
COLLECTION_NAME='WAFERSENSOR'

df=pd.read_csv("D:\Sensor_fault\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)