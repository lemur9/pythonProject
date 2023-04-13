from pymysql import Connection

connection = Connection(host="localhost", user="root", password="123456", port=3306)
# print(connection.get_server_info())

cursor = connection.cursor()
connection.select_db("test")
cursor.execute("create table test_pymysql(id int)")