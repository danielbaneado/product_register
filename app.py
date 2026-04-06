import services_s3 as services
op= True
inventory= []

while op!= 9:
    try:
        op= int(input("\nProduct register\n 1) Add product\n 2) Show inventory\n 3) Calculate stadistics\n 4) Search product\n 5) Update product\n 6) Delete product\n 7) Overwrite/append to CSV\n 8) Charge CSV\n 9) Exit\n >> "))
        if op not in range(1, 10):
            raise ValueError
    except:
        print("Invalid option, please select a valid one.")
        continue
    if op== 1:
        try:
            to_add= int(input("How many products do you want to add?\n >> "))
            if to_add < 0:
                raise ValueError
        except:
            print("Invalid quantity!")
            continue
        for i in range(to_add):
            name= input("Type product name\n >> ").lower()
            try:
                price= float(input("Type product price\n >> "))
                if price <= 0:
                    raise ValueError 
            except:
                print("Invalid price! Try again")
                continue
            try:
                stock= int(input("Type product stock\n >> "))
                if stock <= 0:
                    raise ValueError 
            except:
                print("Invalid stock! Try again")
                continue
            services.add_product(inventory, name, price, stock)
    elif op== 2:
        services.see_inventory(inventory) 
    elif op== 3:
        services.calculate_stadistics(inventory)
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
        choose= input("Overwrite or append (o/a)\n >> ")
        services.save_csv(inventory, choose)
    elif op== 8:
        inventory= services.charge_csv()
    elif op== 9:
        print("Thanks for use our services!")
