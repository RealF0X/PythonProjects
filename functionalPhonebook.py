from urllib.response import addinfo
from phoneModule import *


phoneBook = []  
while True :
    phoneMenu = print(" 1)Add User \n 2)Search User \n 3)Delte User \n 4)Show All \n 5)About App \n 0)Exit The Phone Book")
    userChoice = input("Type a Number between 0 - 5 : ")
    
    #Condition For Adding Numbers
    if userChoice == "1" :
       print(addinfo(phoneBook))