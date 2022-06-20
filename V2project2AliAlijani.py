#Asking The User For Their Password
userPassword = input("\n Hello , Pls Enter A Password : ")

#1)Condition So The Password is 8 Characters or More Than 8 Characters
if len(userPassword) >= 8 :
  
   #2)Condition So The Password isn't Consisted of Only Space
   if (allSpace := userPassword.isspace()) == False :
       
       #3)Condition For AllNum(Only Numbers & Alphabetics With No Space Between Them)
       if userPassword.isalnum() :
           
           #4)Condition so That Password Doesn't Start With Numbers
           if (digitFirstLetter := userPassword[0].isdigit()) == False :
              
               #Hashing The Password With Join
               hashUserPassword = '$#'.join(userPassword)
               print(f"\n Congratulation , Your New Password : {hashUserPassword} , Was Set \n")
           
           #4)
           else :
               print('\n Your Password Shouldn\'t Start With Digits \n')   
       #3)
       else:
           print('\n Your Password Should Only Consist of Numbers & Alphbetics \n Also it Shouldn\'t Have Space Anywhere in it \n')    
           
   #2)        
   else :
       print('\n Your Password Shoudn\'t Consist of Only Space. \n') 
#1)        
else:
    print('\n Your Password Should Have At Least 8 Characters. \n')
    
