import mysql.connector
connection = mysql.connector.connect(user = "root", database = "root", password = "Boopybozo8")
connection.close()
testQuery = (“SELECT * FROM clothing”)

cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()

connection.close()