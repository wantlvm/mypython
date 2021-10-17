import pymysql
db=pymysql.connect(host='49.235.251.113',
                   user='root',
                   password='123456',
                   database='test',
                   charset='utf8',
                   cursorclass=pymysql.cursors.DictCursor)
#创建游标对象
cursor=db.cursor()
#准备sql语句
sql ='select version()'
#执行sql语句
cursor.execute(sql)
#提取结果
data=cursor.fetchall()
#关闭数据库连接
db.close()
print(data)