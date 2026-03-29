op = True
inventory = []

def add_product(inventory, name, price, stock):
    inventory.append({"Product": name, "Price": price, "Stock": stock})
    print(name, "successfully added!")
    return inventory
    
def see_inventory(inventory):  
    if not inventory:  
        print("There's no products added yet!")
        return
    print("Current product list")
    for product in inventory:  
        print("-" * 30)
        for qualities, details in product.items():
            print(qualities, "->", details) 

def calculate_totals(inventory):
    if not inventory:
        print("There's no products added yet!")
        return
    inventory_total= []   
    overall= 0  
    product_quantity= 0  
    for product in inventory:  
        product_quantity+= 1  
        inventory_total.append(product["Price"] * product["Stock"]) 
    print("Overall", "\n", "-" * 30)
    for total in inventory_total: 
        overall+= total
    print("Inventory total ->", overall, "\n", "-" * 30, "\nProducts added ->", product_quantity)

def search_product(inventory, pname):
    if not inventory:  
        print("There's no products added yet!")
        return
    for product in inventory:
        for qualities, details in product.items():
            if pname!= product["Product"]:
                continue
            if qualities== "Product":
                continue
            print(qualities, "->", details)

def update_product(inventory, uname, new_price, new_stock):
    if not inventory:  
        print("There's no products added yet!")
        return
    for product in inventory:
        if product["Product"]== uname:
            product["Price"]= new_price
            product["Stock"]= new_stock
            print(uname, "successfully updated.")
    return inventory
    
def delete_product(inventory, dname):
    if not inventory:  
        print("There's no products added yet!")
        return
    for product in inventory:
        if product["Product"]== dname:
            inventory.remove(product)
            print(dname, "successfully deleted.")

while op!= 7:
    op= int(input("\nProduct register\n 1) Add product\n 2) Show inventory\n 3) Calculate stadistics\n 4) Search product\n 5) Update product\n 6) Delete product\n 7) Exit\n >> ")) 
    if op== 1:
        product_to_add= int(input("How many products do you want to add?\n >> "))
        for i in range(product_to_add):
            name= input("Type product name\n >> ").lower()
            price= float(input("Type product price\n >> "))
            stock= int(input("Type product stock\n >> "))
            add_product(inventory, name, price, stock)
    elif op== 2:
        see_inventory(inventory) 
    elif op== 3:
        calculate_totals(inventory)
    elif op== 4:
        pname= input("Type product name to search\n >> ").lower()
        search_product(inventory, pname)
    elif op== 5:
        uname= input("Type product name to update\n >> ")
        new_price= float(input("Type new product price\n >> "))
        new_stock= int(input("Type new product stock\n >> "))
        update_product(inventory, uname, new_price, new_stock)
    elif op== 6:
        dname= input("Type product name to delete\n >> ").lower()
        delete_product(inventory, dname)
    elif op== 7:
        print("Thanks for use our services!")