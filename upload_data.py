from pymongo.mongo_client import MongoClient
import pandas as pandas
import json

uri="mongodb+srv://dbuser:dbpassword@cluster0.zo37guz.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(uri)

DATABASE_NAME='Project'
COLLECTION_NAME="waferfault"

csv_file_path="./notebooks/data/wafer_23012020_041211.csv"
df=pd.read_csv(csv_file_path)
df=df.drop("Unamed:0",axis=1)

json_records=json.loads(df.T.to_json()).values()
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)