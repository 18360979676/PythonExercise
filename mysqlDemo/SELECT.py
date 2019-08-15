__author__ = 'Administrator'
# 'Administrator' 为预定义的变量，为你当前登录的计算机用户名

from mysql.connector import Connect

mydb = Connect(
    host="localhost",  # 数据库主机地址
    user="root",   # 数据库用户名
    passwd="123456",    # 数据库密码
    database="runnoob_db"
)
mycursor = mydb.cursor()

mycursor.execute("select id, url from sites")

myresult = mycursor.fetchall(3)

for x in myresult:
    print(x)
