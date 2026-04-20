import mysql.connector

dbconnect = mysql.connector.connect(
    host="aDELLe-MTC",
    user="root",
    password="SQLservermanagement!",
    port=3306
)

print(dbconnect)