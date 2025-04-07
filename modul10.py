import os
from datetime import date as Date
from datetime import datetime
import datetime
import time

os.system('cls')

x = datetime.datetime.now() 
print(x.strftime("%Y)"))
print(x.strftime("%A)"))
print(x.strftime("%B)"))
print(x.strftime("%d)"))


#print(x.day)
#print(x.month)
#print(x.year)


input("Starta: ")
start = time.time()

input("Stoppa: ")
print(f"Tid: {time.time() - start:.2f} sek")
    

while True:
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"), end="\r")  
        time.sleep(1)  

