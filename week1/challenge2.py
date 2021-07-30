from datetime import datetime
import json

class Person():
    def __init__(self, name, identityNumber, birthDate ):
        self.name=name
        self.identityNumber = identityNumber
        self.birthDate = birthDate

def sortPeopleByBirthDate():

    People = []
    count =  int(input("Insert number of people inputs : "))    
    #Bucle for input data
    for a in range(count): 

        name =  str(input("Insert Name : "))
        identityNumber =  str(input("Insert Identity Document Number : "))
        birthDate =  str(input("Insert Birth Date (mm/dd/yyyy) : "))
        birthDate_Temp = datetime.strptime(birthDate, '%m/%d/%Y').date()

        personTemp = Person(name,identityNumber,birthDate_Temp)
        People.append(personTemp)
        print("============================")
    #Sort people by birth date
    People.sort(key=lambda res: res.birthDate, reverse=True )
    #Print
    for a in People:
        jsonStr = json.dumps(a.__dict__,default=str)
        print(jsonStr)


sortPeopleByBirthDate()