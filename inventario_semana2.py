op= True
inventory= []
def add_product(inventory):
    try:
        name= input("Type product name\n >> ")
        price= float(input("Type product price\n >> "))
        stock= int(input("Type product stock\n >> "))
        inventory.append({"Name": name, "Price": price, "Stock": stock})
    except:
        print("Invalid value! Try again")
    return products
        
while op!= 4:
    try:
        op= int(input("Product register\n 1) Add product\n 2) Show inventory \n 3) Calculate stadistics\n 4) Exit\n >> "))
        if op== 1:
            add_product(products)
        elif op== 2:
            pass
        elif op== 3:
            pass
        elif op== 4:
            pass
        else:
            raise ValueError
    except:
        print("Invalid option! Select it again")