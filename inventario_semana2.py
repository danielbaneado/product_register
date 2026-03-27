op = True  # Menu control variable
inventory = []  # List that will store products (dictionaries)

def add_product(inventory):  # Function to add a product to the inventory
    name = input("Type product name\n >> ")  # Requests product name
    try:
        price = float(input("Type product price\n >> "))  # Converts price to float
        stock = int(input("Type product stock\n >> "))  # Converts stock to integer
    except:
        print("There's invalid data to register this product. Please register it again")  # Input error handling
        return  # Exits function without adding anything
    inventory.append({"Product": name, "Price": price, "Stock": stock})  # Adds product as dictionary
    print(name, "succesfully added!")  # Confirmation message
    return inventory  # Returns updated inventory (not strictly necessary)

def see_inventory(inventory):  # Function to display all products
    if not inventory:  # Checks if list is empty
        print("There's no products added yet!")
        return
    print("Current product list")
    for product in inventory:  # Iterates over each product
        print("-" * 30)
        for names, details in product.items():  # Iterates over key-value pairs
            print(names, "->", details)  # Displays each product attribute

def calculate_totals(inventory):  # Calculates total inventory value and product count
    if not inventory:  # Empty list validation
        print("There's no products added yet!")
        return
    inventory_total = []  # List to store totals per product
    overall = 0  # Total value accumulator
    product_quantity = 0  # Product counter

    for product in inventory:  # Loops through each product
        product_quantity += 1  # Increments counter
        inventory_total.append(product["Price"] * product["Stock"])  # Calculates total per product

    print("Overall", "\n", "-" * 30)
    for total in inventory_total:  # Sums all individual totals
        overall += total
    print("Inventory total ->", overall, "\n", "-" * 30, "\nProducts added ->", product_quantity)  # Final result

while op != 4:  # Main menu loop (runs until exit option is selected)
    try:
        op = int(input("\nProduct register\n 1) Add product\n 2) Show inventory \n 3) Calculate stadistics\n 4) Exit\n >> "))  # Option input

        if op == 1:
            add_product(inventory)  # Calls function to add product
        elif op == 2:
            see_inventory(inventory)  # Calls function to display inventory
        elif op == 3:
            calculate_totals(inventory)  # Calls function to calculate statistics
        elif op == 4:
            print("Thanks for use our services!")  # Exit message
        else:
            raise ValueError  # Forces error if option is invalid
    except:
        print("Invalid option! Select it again")  # Menu error handling
