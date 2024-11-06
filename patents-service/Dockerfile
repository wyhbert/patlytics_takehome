# Flask Dockerfile
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制并安装项目依赖
COPY requirements.txt .
# RUN pip install -r requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 复制代码到容器
COPY . .

# 暴露 Flask 默认端口
EXPOSE 5001

# 启动 Flask 应用
CMD ["python", "app.py"]
