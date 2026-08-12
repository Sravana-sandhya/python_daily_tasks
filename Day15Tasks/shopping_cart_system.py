#Q3 : Shopping Cart System 
# Scenario: A user adds items to a shopping cart. 
# Task: 
# ● Store items in a list 
# ● Convert to set to remove duplicates 
# ● Use loop + condition to calculate total cost 
# ● Handle invalid input using try-except
items = ["Apple", "Milk", "Apple", "Bread"]
unique_items = set(items)
total = 0
try:
   for item in unique_items:
    price = int(input("Enter price for " + item + ": "))
    if price > 0:
      total = total + price
    else:
        print("Invalid price")
   print("Unique items in cart:", unique_items)
   print("Total cost: ", total)
except ValueError:
    print("Invalid input. Please enter a numeric value for price.")



  