import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd  ="sherrygill123",
    database = "store"
)

my_cursor = mydb.cursor()
#
# my_cursor.execute("USE STORE;")
# my_cursor.execute("SELECT * FROM customers")
# my_cursor.commit()
#
# for db in my_cursor:
#     print(db)

#my_cursor.execute("CREATE TABLE users (name VARCHAR(20), email VARCHAR(50), age INT, user_id INT AUTO_INCREMENT, PRIMARY KEY(user_id))")
#my_cursor.execute("SHOW TABLES")

#my_cursor.execute("INSERT INTO users (name, email,age) VALUE('Joe', 'joe@gmail.com', 24), ('Bob', 'bob@gmail.com', 10)")

# sqlStuff = "INSERT INTO users (name,email,age) VALUES (%s,%s,%s)"
# record1 = ('Joe', 'joe@gmail.com', 24)
#
# my_cursor.execute(sqlStuff, record1)
# mydb.commit()
# sql = '''
#     UPDATE users
#     SET age = 100
#     '''
my_cursor.execute("SELECT * FROM users")
myresult = my_cursor.fetchall()

for row in myresult:
    print(row)
