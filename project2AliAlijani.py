#Password Entry




#Warning
#This Entry Has Mistakes Pls Refer To Version2 Of This Code










userPassword = input("Pls Enter A Password : ")

#1)if for 8 Characters
if len(userPassword) >= 8 :
  
   #2)condition so pass isn't all space
   spaceChecking = userPassword.isspace()
   if spaceChecking == False :
       
       #3)Condition For AllNum
       if userPassword.isalnum :
           
           #4)Condition so That Password Doesn't Start With Numbers
           digitCheking = userPassword.isdigit()
           if digitCheking == False :
               hashPassword = '$'.join(userPassword)
               print(f"Your Password {hashPassword} Was Set")
           #4)
           else :
               print('Your Password Shouldn\'t Start With Digits ')   
       #3)
       else:
           print('Your Password Should Only Consist of Numbers & Alphbetics')    
           
   #2)        
   else :
       print('Your Password Shoudn\'t be All Space.') 
#1)        
else:
    print('Your Password Should Have At Least 8 Characters.')
    
