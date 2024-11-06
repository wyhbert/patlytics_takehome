import json
from pymongo import MongoClient

# MongoDB连接参数
username = 'test'
password = '123456'
host = 'localhost'
port = 27017
database_name = 'quant'
collection_name = 'patents'

# 连接到MongoDB
client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/?authSource=quant')


# 选择数据库和集合
db = client[database_name]
collection = db[collection_name]


# 导入JSON文件
with open('patents.json') as file:
    data = json.load(file)
    # 如果数据是一个列表，可以使用insert_many
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

print("数据已成功导入MongoDB！")
