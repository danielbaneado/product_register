import services_s3
op= True
inventory= []

while op!= 7:
    op= int(input("\nProduct register\n 1) Add product\n 2) Show inventory\n 3) Calculate stadistics\n 4) Search product\n 5) Update product\n 6) Delete product\n 7) Exit\n >> ")) 
    if op== 1:
        product_to_add= int(input("How many products do you want to add?\n >> "))
        for i in range(product_to_add):
            name= input("Type product name\n >> ").lower()
            price= float(input("Type product price\n >> "))
            stock= int(input("Type product stock\n >> "))
            services.add_product(inventory, name, price, stock)
    elif op== 2:
        services.see_inventory(inventory) 
    elif op== 3:
        services.calculate_totals(inventory)
    elif op== 4:
        pname= input("Type product name to search\n >> ").lower()
        services.search_product(inventory, pname)
    elif op== 5:
        uname= input("Type product name to update\n >> ")
        new_price= float(input("Type new product price\n >> "))
        new_stock= int(input("Type new product stock\n >> "))
        services.update_product(inventory, uname, new_price, new_stock)
    elif op== 6:
        dname= input("Type product name to delete\n >> ").lower()
        services.delete_product(inventory, dname)
    elif op== 7:
        print("Thanks for use our services!")