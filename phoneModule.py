#Add Function   
def addInfo(myList):
    '''For Adding Name & Number To PhoneBook'''
    # return( userName + " : " + UserNumber)
    nameInput = input("Pls Enter The Name : ").lower()
    numberInput = input("Pls Enter The Number : ").lower()
    fullInfo = nameInput + ":" + numberInput
    return(myList.append(fullInfo))
    
    
    

#Search Function
def searchInfo(myList) :
    userSearch=input(f"\nPls Enter The Name or The Number You Want to Search : ").lower()
    for i in myList : 
        if userSearch == i.split(":")[0] or userSearch == i.split(":")[1] :
            return(f"\nYour Search is {i} \n")
        else :
            return("\nNot Found\n") 
       


#Delete Function
def deleteInfo(myList) :
    deleteName = input("\nPls Enter The Name or The Number You Want to Delete :").lower()
    for i in myList : 
        if deleteName == i.split(":")[0] or deleteName == i.split(":")[1]:
                myList.remove(i)     
        else :
            return("\nNot Found\n")  
        
        
                  
        
     

