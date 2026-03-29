def add_product(inventory, name, price, stock):
    """
    Adds product name, price and stock in a new dictionary at inventory list.
    """
    inventory.append({"Product": name, "Price": price, "Stock": stock})
    print(name, "successfully added!")
    
def see_inventory(inventory):
    """
    If there's no products, program returns to main menu, else, function iterates in product list, showing all qualities.
    """
    if not inventory:  
        print("There's no products added yet!")
        return
    print("Current product list")
    for product in inventory:  
        print("-" * 30)
        for qualities, details in product.items():
            print(qualities, "->", details) 

def calculate_totals(inventory):
    """
    Same return as see_inventory.
    Calculates an overall by all products price and stock, also shows the number of added products.
    """
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
    cart= (overall, product_quantity)
    return cart

def search_product(inventory, pname):
    """
    Searchs product by name, if the name of iterated product doesnt match with seeked product, program skip this one.
    """
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
    """
    Modifies price and stock for product to update, receiving this parameters and rewriting dictionary.
    """
    if not inventory:  
        print("There's no products added yet!")
        return
    for product in inventory:
        if product["Product"]== uname:
            product["Price"]= new_price
            product["Stock"]= new_stock
            print(uname, "successfully updated.")
    
def delete_product(inventory, dname):
    """
    Iterates in inventory list and delete product searching by name.
    """
    if not inventory:  
        print("There's no products added yet!")
        return
    for product in inventory:
        if product["Product"]== dname:
            inventory.remove(product)
            print(dname, "successfully deleted.")
