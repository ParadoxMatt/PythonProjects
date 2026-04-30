import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQLservermanagement!",
    port=3306,
    database='mypythondatabase'
)

dbc = mydb.cursor()

'''
sql = "INSERT INTO customers (name,number) VALUES (%s,%s)"
val = [
    ("Matthew","0783674491"),
    ("Charlene","0447654317"),
    ("Nigel","0637653173"),
    ("Mavis","0826547612"),
    ("Mutsa","0827635478"),
    ("Tadiwa","0836735415")
]
'''

dbc.execute("SELECT * FROM customers")

result = dbc.fetchall()

for i in result:
    print(i)
