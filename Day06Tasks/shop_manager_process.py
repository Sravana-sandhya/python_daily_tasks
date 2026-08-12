# Q2: Develop a Python program for a small shop to process customer purchases. Store product 
# names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
# and product details using tuples. Create functions to display products, add items to the cart, and 
# calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 
# Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError 
# (calculation errors), TypeError (wrong data types in the cart), and NameError (when a product 
# name entered by the user does not exist). 
# Example Output: 
# 1. Display Products 
# 2. Add Item to Cart 
# 3. View Total Bill 
# 4. Exit 
# Enter choice: 1 
# Available Products: 
# Pen : 10 
# Notebook : 50 
# Pencil : 5 
# 1. Display Products 
# 2. Add Item to Cart 
# 3. View Total Bill 
# 4. Exit 
# Enter choice: 2 
# Enter product name: Pen 
# Enter quantity: 3 
# Item added to cart successfully. 
# 1. Display Products 
# 2. Add Item to Cart 
# 3. View Total Bill 
# 4. Exit 
# Enter choice: 2 
# Enter product name: Notebook 
# Enter quantity: 2 
# Item added to cart successfully. 
# 1. Display Products 
# 2. Add Item to Cart 
# 3. View Total Bill 
# 4. Exit 
# Enter choice: 3 
# Items in Cart: 
# Pen x 3 
# Notebook x 2 
# Total Bill: 130 
# Example Exception Outputs 
# ValueError 
# Enter quantity: abc 
# Invalid quantity! Please enter a number. 
# NameError 
# Enter product name: Eraser 
# Product not found in store. 
# TypeError 
# Cart data type error. 
# ZeroDivisionError 
# # Calculation error: division by zero.
# Dictionary (Product : Price)
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

# List (Cart)
cart = []

# Set (Categories)
categories = {"Stationery"}

# Tuple (Product Details)
product_details = (
    ("Pen", 10),
    ("Notebook", 50),
    ("Pencil", 5)
)

# Recursive function to calculate total bill
def total_bill(cart, index=0):
    if index == len(cart):
        return 0
    return cart[index][2] + total_bill(cart, index + 1)

# Function to display products
def display_products():
    print("Available Products:")
    for product, price in products.items():
        print(product, ":", price)

# Function to add item to cart
def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        total = products[name] * quantity

        cart.append((name, quantity, total))

        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")

# Function to view total bill
def view_bill():
    try:
        if len(cart) == 0:
            raise ZeroDivisionError

        print("Items in Cart:")

        for item in cart:
            if not isinstance(item, tuple):
                raise TypeError

            print(item[0], "x", item[1])

        total = total_bill(cart)

        print("Total Bill:", total)

    except ZeroDivisionError:
        print("Calculation error: division by zero.")

    except TypeError:
        print("Cart data type error.")

# Main Program
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_bill()

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")