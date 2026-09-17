#benjamin copier debugging with the debugger
# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? "))# it was acting as if it was a string.

total = price * quantity
total2=int(total)#made into an integer
discounted_total = total2 - 2 * 0.10 #replaced the string total with the int total two

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name)#renamed the variable
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(discounted_total))#the total before tax was not the total it was just the price.
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")#added a parenthesis.