import pymysql

db=pymysql.connect(host='localhost',user='root',password='asd369258',port=3306)
cursor=db.cursor()
cursor.execute('SELECT VERSION()')
data=cursor.fetchone()
print(data)
cursor.execute()