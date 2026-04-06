import csv
import os

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

def calculate_stadistics(inventory):
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
        
    print("Most expensive product")
    expensive= sorted(inventory, key=lambda x: x["Price"], reverse=True)
    for qualities, details in expensive[0].items():
        if qualities== "Stock":
            continue
        print(qualities, "->", details) 
            
    print("-" * 30)
    print("Product with more stock")
    stock= sorted(inventory, key=lambda x: x["Stock"], reverse=True)
    for qualities, details in stock[0].items():
        if qualities== "Price":
            continue
        print(qualities, "->", details) 
        
    print("-" * 30)
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

def save_csv(inventory, choose):
    """
    Saves the current inventory to products.csv
    o: overwrites the file with the full current inventory
    a: appends only new products
    """
    if not inventory:
        print("There's no products to save!")
        return

    fieldnames= ["Product", "Price", "Stock"]
    choose= choose.strip().lower()

    if choose== "o":
        with open("products.csv", "w", newline="") as file:
            writer= csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(inventory)
        print("products.csv successfully overwritten.")

    elif choose== "a":
        #load existing products from file (if it exists) to detect duplicates
        existing_names= set()
        if os.path.exists("products.csv"):
            try:
                with open("products.csv", "r", newline="") as file:
                    reader= csv.DictReader(file)
                    for row in reader:
                        existing_names.add(row["Product"].lower())
            except Exception as e:
                print(f"Warning: could not read existing file ({e}). Appending all products.")

        #filter out products already in the file
        new_products= [p for p in inventory if p["Product"].lower() not in existing_names]

        if not new_products:
            print("No new products to append — all are already in products.csv.")
            return

        file_exists= os.path.exists("products.csv")
        with open("products.csv", "a", newline="") as file:
            writer= csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()  #write header only if file is being created
            writer.writerows(new_products)
        print(f"{len(new_products)} new product(s) successfully appended to products.csv.")

    else:
        print("Invalid option. Please enter 'o' to overwrite or 'a' to append.")

            
def charge_csv():
    """
    Loads products from products.csv into the inventory list.
    Handles the case where the file does not exist yet.
    """
    try:
        with open("products.csv", "r", newline="") as file:
            reader= csv.DictReader(file)
            inventory= list(reader)
            for product in inventory:
                product["Price"]= float(product["Price"])
                product["Stock"]= int(product["Stock"])
            print("products.csv successfully loaded.")
            return inventory
    except FileNotFoundError:
        print("products.csv not found. Start by adding products and saving them first.")
        return []
    except Exception as e:
        print(f"Error loading products.csv: {e}")
        return []
                
