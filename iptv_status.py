import pymysql
db = pymysql.connect("10.10.100.244", "root","mySql_r00t", "stalker_db")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("Версия MySQL : %s " + str(data))
db.close()

