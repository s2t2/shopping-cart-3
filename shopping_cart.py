# shopping_cart.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


from dotenv import load_dotenv
import os


total_price = 0
selected_items = []


id_list = []
for p in products:
    id_list.append(str(p["id"]))

#unique_ids = list(set(id_list))

while True:
    cashier_input = input("Please input a product identifier: ")
    if cashier_input == "DONE":
        break
    elif cashier_input not in id_list:
        print ("Sorry, item not found. Please try again...")
    else:
        selected_items.append(cashier_input)
 
#print(selected_items)

print("-----------------------------------------------------------")
print("GU Healthy Foods")
print("3700 O ST NW Washington DC")
print("Phone: (202)-495-3439")
print("Website: www.guhealthyfoods.com")
print("-----------------------------------------------------------")

import datetime
purchase_time = datetime.datetime.now()
print("Checkout at: " + purchase_time.strftime("%Y-%m-%d %I:%M %p"))
print("-----------------------------------------------------------")


print("Selected products: ")
for cashier_input in selected_items: 
    matching_products = [p for p in products if str(p["id"]) == str(cashier_input)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    price_usd = "${0:.2f}".format(matching_product["price"])
    print("... " + matching_product["name"] + " (" + str(price_usd) + ")")

print("-----------------------------------------------------------")
total_price_usd = "${0:.2f}".format(total_price)
print("Subtotal: " + str(total_price_usd))

#FURTHER CHALLENGE: configuring sales tax rate
#Code Source for this challenge: Online notes on dotenv package:
#https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/dotenv.md

load_dotenv() 

tax_rate_input = float(os.environ.get("tax_rate"))
tax = total_price*(tax_rate_input)
tax_usd = "${0:.2f}".format(tax)
print("Tax: " + str(tax_usd))

total_amount = total_price + tax
total_amount_usd = "${0:.2f}".format(total_amount)
print("Total: " + str(total_amount_usd))

print("-----------------------------------------------------------")
print("Thanks for shopping with us!")
print("Hope to see you again soon.")
print("-----------------------------------------------------------")





        #product_names = [p["name"] for p in products]
        #x = ["hello" for p in products]