# python-food-ordering-system
This is an take away ordering system where the main items offered are pizzas and the pastas.
The food_menu.txt acts like the database for the items sold in the shop. This stores the food item by its number,name and price.
The first 7 seven lines of the program displays the welcome message to the customers.The information included in the welcome message is the name of show and a welcoming new customers to buy food.
line nine opens the food-menu.txt file for the purpose of reading the content of the food items only.The file is opened in the read mode only meaning one can only see what is in the file but cannot edit the file.
line 10 Displays the heading of the food items details, that is food-no,name and price.
line 11 to 16 displays the menu to the customer by reading all that is stored in the food-menu.txt file.
line 18 initializes total_cost of customer's order to zero. This is total_cost is the one that is used to display the grand total after the customer has finished making the order.
line 19, prompts the user to enter no of food he would like to order as displayed by the me.One can enter 1 to order for '1 Large Pizza' and so on.
line 21 to 30 , enable the user to order all that he wants as long as the input is not equal to quit which is represented by "Q".The cost of item ordered is update as the users continues to order until she enters "Q" to quit the program.

line 32 displays the Grand total to the user after he is done with ordering.
line 33 displays a good-bye message to the user
line 34 closes the food-menu.txt file as this marks the end of the program.


