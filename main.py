print(" **************************************** ")
print("|    Amazing Pizza and Pasta Pizzeria    |")
print("|    Ordering System                     |")
print(" ***************************************** ")
print("\n")
print("Welcome to our takeway ordering system.")
print("Here is our menu below")

file = open("food-menu.txt","r")
print("Food No\t\tName\t\t\tPrice")
for items in file:
    food_item = items.split(";")
    food_code = food_item[0]
    food_name = food_item[1]
    food_price = float(food_item[2])
    print(food_code+"\t\t"+food_name+"\t\t"+str(food_price)+" AUD")

total_cost = 0
order_code = input("Enter the no of food you would like to order: ")

while order_code != "Q":
    for item in file:
        food_item = item.split(";")
        food_code = food_item[0]
        food_name = food_item[1]
        food_price = float(food_item[2])
        if food_code == order_code:
            print(food_code+"\t\t"+food_name+"\t\t"+str(food_price)+" AUD")
            total_cost = total_cost + food_price
        
    order_code = input("Enter another no to continue ordering or Q to quit: ")
    
print("The total cost is:"+ str(total_cost))
print("Thank you for your Ordering with us")
file.close()
