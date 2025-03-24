import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rishabh@124",
  database="college"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE teachers (name VARCHAR(255), address VARCHAR(255))")

print(mydb) 