import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 定义阈值
threshold = 0.1

# 读取公司和产品数据
with open('company_products.json', 'r', encoding='utf-8') as file:
    companies_data = json.load(file)

# 读取专利数据
with open('patents.json', 'r', encoding='utf-8') as file:
    patents = json.load(file)

# 找到指定公司的产品
def get_products_by_company(company_name):
    for company in companies_data['companies']:
        if company['name'] == company_name:
            return company['products']
    return []



# 新增函数：查找指定公司下使用指定专利的相关产品
def find_related_products_by_patent(patent_id, company_name):
    # 获取指定专利的信息
    patent_info = next((patent for patent in patents if patent['id'] == patent_id), None)
    
    if patent_info is None:
        print(f"Patent ID {patent_id} not found.")
        return []
    single_patents = [patent_info]

    # 找到指定公司的产品
    products = get_products_by_company(company_name)

    # 提取产品描述和专利描述
    product_descriptions = [f"{product['description']} {product['name']}" for product in products]
    patent_descriptions = [f"{patent['title']} {patent['abstract']}" for patent in single_patents]

    # 创建 TF-IDF 向量
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(product_descriptions + patent_descriptions)

    # 计算相似度
    product_vectors = tfidf_matrix[:len(products)]
    patent_vectors = tfidf_matrix[len(products):]
    similarity_matrix = cosine_similarity(product_vectors, patent_vectors)

    # 记录每个产品的总相似度分值及侵权专利信息
    product_scores = {product['name']: {'score': 0, 'patents': []} for product in products}


    result = []
    # 计算每个产品的侵权分值
    for i, product in enumerate(products):
        for j, patent in enumerate(single_patents):
            similarity_score = similarity_matrix[i][j]
            if similarity_score > threshold:
                product_scores[product['name']]['score'] += similarity_score
                product_scores[product['name']]['patents'].append({
                    'patent_id': patent['id'],
                    'patent_title': patent['title'],
                    'similarity_score': similarity_score
                })
                result.append({
                    'company_name': company_name,
                    'product_name': product['name'],
                    'patent_id': patent['id'],
                    'patent_title': patent['title'],
                    'similarity_score': similarity_score
                })

    # 找到侵权分值最高的两种产品
    return result


def getTopTwoInfringedPatentUnderCompany(company_name):

    # 找到指定公司的产品
    products = get_products_by_company(company_name)

    # 提取产品描述和专利描述
    product_descriptions = [f"{product['description']} {product['name']}" for product in products]
    patent_descriptions = [f"{patent['title']} {patent['abstract']}" for patent in patents]

    # 创建 TF-IDF 向量
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(product_descriptions + patent_descriptions)

    # 计算相似度
    product_vectors = tfidf_matrix[:len(products)]
    patent_vectors = tfidf_matrix[len(products):]
    similarity_matrix = cosine_similarity(product_vectors, patent_vectors)

    # 记录每个产品的总相似度分值及侵权专利信息
    product_scores = {product['name']: {'score': 0, 'patents': []} for product in products}


    # 计算每个产品的侵权分值
    for i, product in enumerate(products):
        for j, patent in enumerate(patents):
            similarity_score = similarity_matrix[i][j]
            if similarity_score > threshold:
                # product_scores[product['name']]['score'] += similarity_score
                product_scores[product['name']]['patents'].append({
                    'patent_id': patent['id'],
                    'publication_number': patent['publication_number'],
                    'patent_title': patent['title'],
                    'similarity_score': similarity_score
                })

    # 找到侵权分值最高的两种产品
    product_scores = sorted(product_scores.items(), key=lambda x: x[1]['score'], reverse=True)
    list = []
    for item in product_scores:
        entity = {
            'featureName': item[0],
            'patentGroup': {
                'patents': item[1]['patents']
            }
        }
        print(entity)
        list.append(entity)
    return list


    # # 输出结果
    # print("Top Products with Highest Infringement Scores:")
    # for product, info in top_products:
    #     print(f"Product: {product}, Infringement Score: {info['score']:.4f}")
    #     for patent in info['patents']:
    #         print(f"  - Patent ID: {patent['patent_id']}, Title: {patent['patent_title']}, Similarity Score: {patent['similarity_score']:.4f}")
