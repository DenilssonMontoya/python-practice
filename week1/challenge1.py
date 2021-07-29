from datetime import datetime


name =  str(input("Insert Name : "))
age =  int(input("Insert Age : "))

now = datetime.now()
message = ""


if(age <= 0):
    message = "Wrong age.".format(name)
elif(age >= 18):
    message = "{:s},you can do nothing!".format(name)
else:
    if(now.hour >= 18):
        message = "{:s},you must go to bed.".format(name)
    else:
        message = "{:s},you must do your homework.".format(name)

print(message)    