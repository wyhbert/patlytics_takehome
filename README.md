# 共三个项目
1. patents-service，是一个python项目，使用了flask框架，用于提供验证公司是否有专利侵权的服务
2. patlytics-web，是一个基于springboot搭建的web框架，是一个比较常用的快速启动web项目的骨架项目
3. patlytics-web/ruoyi-ui，一个基于vue3和element-ui的前端框架

# 环境准备
1. java -version
java version "1.8.0_401"

2. mvn -v
Apache Maven 3.8.6

3. node -v
v20.16.0

4. python
Python 3.11.5

5. mongodb
版本：mongodb-6.0.14
启动命令：进入mongodb-6.0.14/bin路径，执行./mongod --config ../mongod.conf

6. mysql
版本mysql8.2.0
我是用docker启动，参考docker.png


7. redis
可在docker中安装最新版

# 项目启动
1. 进入patents-service，执行python app.py，启动python项目，端口为5000
项目中的数据源已导入mongo库，脚本可见importPatent.py和importCompany.py
实际生产环境可通过api调用外部接口获取专利信息，同步到Mongo库中

2. patlytics-web已打包成patlytics-web.jar，可执行java -jar patlytics-web.jar & 启动

3. 进入patlytics-web/ruoyi-ui npm run dev，启动后打开http://localhost:1024/index。
账号：admin，密码：admin123
如果要在生产环境中启动，需要安装nginx，设置反向代理访问后端java服务，这样可以避免跨域问题

1）公司侵权专利查询（公司名称下拉框数据来源mongo库）
company.png
mongo.png
2）查询专利在某家公司可能涉及侵权的产品
company-patent.png
