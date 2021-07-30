from datetime import datetime
import json

class Product():
    def __init__(self, name, description):
        self.name=name
        self.description = description

def insertProduct():

    Products = []
    count =  int(input("Insert number of products to enter : "))    
    #Bucle for input data
    for a in range(count): 

        name =  str(input("Insert product name : "))
        description =  str(input("Insert product description : "))


        productTemp = Product(name,description)
        Products.append(productTemp)
        print("============================")

    return Products

def searchProduct(Products, productName):
    result = "*** Product Not Found ***"
    for a in Products :
        if(a.name == productName):
            result = a.description
            break
    return result
    
    
def manageProducts():
   
   Products = insertProduct()
   #Action
   search = True
   while(search):
       action =  str(input("Input product to search or 0 to exit : "))    
       if(action != "0"):
          productDescription = searchProduct(Products,action)

          print(productDescription)
       else:
          search = False

manageProducts()