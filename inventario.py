products= []
try:
    name= input("Type product name: ")
    price= float(input("Type product price: "))
    stock= int(input("Type product quantity: "))
except:
    print("Invalid value! Try again")
