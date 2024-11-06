from pymongo import MongoClient

# 连接到 MongoDB
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

# 示例产品数据
products = [
    {"name": "S700 Combine Harvester", "description": "Harvester with integrated stalk measurement system"},
]

# 提取产品标题作为查询关键词
for product in products:
    product_title = product['description']
    
    # 使用文本搜索查询匹配的专利
    patent_records = collection.find({
        "": {"$search": product_title}
    })
    
    # 记录匹配的专利信息
    matched_patents = []
    for patent in patent_records:
        matched_patents.append({
            "patent_id": patent['id'],
            "title": patent['title'],
            "description": patent.get('description', '')
        })
    
    # 输出结果
    print({
        'product': product['name'],
        'matched_patents': matched_patents
    })
