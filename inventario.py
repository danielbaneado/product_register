op= True
products= []
def add_and_see(fproducts):
    try:
        name= input("Type product name: ")
        price= float(input("Type product price: "))
        stock= int(input("Type product quantity: "))
        fproducts.append({"Name": name, "Price": price, "Stock": stock})
        final_price= price * stock
        for product in fproducts:
            for names, details in product.items():
                print(names, "-", details)
        print("Final price -", final_price)
    except:
        print("Invalid value! Try again")
        
while op!= "n":
    op= input("Add product (y/n): ").lower()
    if op== "y":
        add_and_see(products)
    elif op== "n":
        print("Bye")
