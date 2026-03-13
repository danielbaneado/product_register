#Inicializar op (option) para el bucle while
op= True
#Lista de productos en que se almacenará cada uno
products= []
#Funcion que recibe la lista products, pasandola como fproducts
def add_and_see(fproducts):
    #bloque try except para manejar la entrada de los tres datos y el cálculo del total
    try:
        #solicita nombre al usuario
        name= input("Type product name: ")
        #solicita precio del producto
        price= float(input("Type product price: "))
        #solicita cantidad
        stock= int(input("Type product quantity: "))
        #los añade como diccionario en la lista de productos
        fproducts.append({"Name": name, "Price": price, "Stock": stock})
        #calcula el costo final
        final_price= price * stock
        #recorre la lista de productos
        for product in fproducts:
            #recorre las claves y valores de cada producto
            for names, details in product.items():
                #los imprime en consola
                print(names, "-", details)
        #muestra el costo final
        print("Final price -", final_price)
    #vuelve a ejecutar el bloque try si se ingresa un valor inválido
    except:
        print("Invalid value! Try again")
#bucle while para seguir añadiendo productos
while op!= "n":
    #pregunta al usuario si seguir añadiendo productos
    op= input("Add product (y/n): ").lower()
    #si escribe y, se ejecuta la funcion recibiendo la lista products
    if op== "y":
        add_and_see(products)
    #si escribe n, el código termina
    elif op== "n":
        print("Bye")
