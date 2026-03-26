op= True
inventory= []
def add_product(inventory):
    name= input("Type product name\n >> ")
    try:
        price= float(input("Type product price\n >> "))
        stock= int(input("Type product stock\n >> "))
    except:
        print("There's invalid data to register this product. Please register it again")
        return
    inventory.append({"Product": name, "Price": price, "Stock": stock})
    print(name, "succesfully added!")
    return inventory

def see_inventory(inventory):
    if not inventory:
        print("There's no products added yet!")
        return
    print("Current product list")
    for product in inventory:
            print("-" * 30)
            for names, details in product.items():
                print(names, "->", details)

while op!= 4:
    try:
        op= int(input("\nProduct register\n 1) Add product\n 2) Show inventory \n 3) Calculate stadistics\n 4) Exit\n >> "))
        if op== 1:
            add_product(inventory)
        elif op== 2:
            see_inventory(inventory)
        elif op== 3:
            pass
        elif op== 4:
            print("Thanks for use our services!")
        else:
            raise ValueError
    except:
        print("Invalid option! Select it again")
