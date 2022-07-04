import os
os.system("cls")

phoneBook = []  
while True :
    phoneMenu = print(" 1)Add User \n 2)Search User \n 3)Delte User \n 4)Show All \n 5)About App \n 0)Exit The Phone Book")
    userChoice = input("Type a Number between 0 - 5 : ")
    
    #Condition For Adding Numbers
    if userChoice == "1" :
        nameInput = input("Pls Enter The Name : ").lower()
        numberInput = input("Pls Enter The Number : ").lower()
        fullInfo = nameInput + ":" + numberInput
        phoneBook.append(fullInfo)
       
    
    #Condition For Search
    elif userChoice == "2" : 
        userSearch = input(f"\nPls Enter The Name You Want to Search : ")
        searchValue = False
        for i in phoneBook : 
            if userSearch == i.split(":")[0] :
                searchValue == True 
                print(f"\nYour Search is {i} \n")
            elif searchValue != True :
                print("\nNot Found\n") 
                break
                     
    #Condition For Delete
    elif userChoice == "3" :
        deleteName = input("\nPls Enter The Name You Want to Delete :").lower()
        for i in phoneBook : 
            if deleteName == i.split(":")[0] or deleteName == i.split(":"):
                phoneBook.remove(i)    
                print(phoneBook)  
            else :
                print("\nNot Found\n")  
                break      
    
    #Print PhoneBook
    elif userChoice == "4" :
        print(phoneBook)    
    
    #Credit
    elif userChoice == "5" :
        print("\nPhoneBook Version 1.006 was Designed by Ali Alijani,You Can Contact me \nwith This Number  09124488875 \n")
    
    #Condition For Exiting The App
    elif userChoice == "0" :
        print("\nGoodbye Hope To See You Soon ")
        break
    
    #Condition For Unauthorized Numbers
    else :
       print("\nPls Enter a Valid Number\n ")
