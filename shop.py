"""
shoppin system:
1. menu to BUY, SELL, REFUND items at this store
2. Make a reciept generator to make every sale unique
3. idk I'll make it up as I go
"""
import mysql.connector

dbconnect = mysql.connector.connect(
    host="localhost",
    user="chiha",
    password="",
)
query = dbconnect.cursor()
query.execute("CREATE DATABASE python_store ")

def choice():
    print("\nWelcome to the Shop\n"    
    "1. Buy items\n" \
    "2. Sell items\n" \
    "3. Refund items\n" \
    "4. Check inventory\n" \
    "5. Exit Program\n")
    return input(": ")

def main():
    option = choice()
    while option != "5":
        if choice == "1":
            buy_items()
        elif choice == "2":
            sell_items()
        elif option == "3":
            refund_items()
        elif option == "4":
            shop_inventory()
    choice()

    exit()

def buy_items(price, item_ID, item_name, reciept_ID):
    pass

def sell_items():
    pass

def refund_items(self, reciept_ID):
    pass

def shop_inventory(price, item_ID, item_name, reciept_ID):
    pass

query.close()
dbconnect.close()