from flask import Flask, request, jsonify
from check import *


app = Flask(__name__)

@app.route('/')
def home():
    return "欢迎来到 Flask 项目！"

@app.route('/api')
def api():
    return {"message": "这是一个 API 接口"}

@app.route('/api/checkCompanyProducts', methods=['POST'])
def check_company_products():
    data = request.get_data()  # 获取请求的 JSON 数据
    # company_name = data.get('companyName')  # 从请求中获取公司名称
    # company_name = 'Walmart Inc.'
    
    # 这里可以添加处理逻辑，例如查询数据库等
    response = getTopTwoInfringedPatentUnderCompany(data.decode('utf-8'))
    return jsonify(response)

@app.route('/api/getInfringingProducts', methods=['POST'])
def get_infringing_products():
    data = request.get_json()  # 获取请求的 JSON 数据
    patent_id = data.get('patentId')
    company_name = data.get('companyName')
    # patent_id = 3
    # company_name = 'John Deere'
    
    # 这里可以添加处理逻辑，例如查询数据库等
    response = find_related_products_by_patent(patent_id, company_name)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)