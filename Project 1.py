#User Name 
userFirstName = input(" Pls Enter Your First Name : ")
userFamilyName = input("Pls Enter Your Family Name :  ")

#Welcome Message
print(f" \n Welcome to This App {userFirstName} {userFamilyName} \n ")

#Menu
print(" 1) ➕ Addition ➡️   + \n 2) ➖ Minus ➡️   - \n 3) ❌ Multipliction ➡️    * \n 4) ➗ division ➡️    /  \n 5) 💪 Exponentiation ➡️    ** \n 6) 👌 Modulus ➡️   %  \n 7) 👋 Exit ➡️   Exit \n")

#Asking for User Numbers & Math operator 
firstNumber = int(input(f"{userFirstName}   pls Enter Your First number  : "))
secondNumber = int(input(f"{userFirstName}  pls Enter Your Second number : "))
mathRequest = input("Which Option From The Menu Would You Like To Choose (You Can Either Type The Number Of the Action From The Menu or The Name of Math Action From The Menu) :  ")


#if 
if  mathRequest == "addition" or mathRequest == "Addition" or mathRequest == "1" :
    userAddition = firstNumber + secondNumber
    print(f"{userFirstName} The Addition of {firstNumber} & {secondNumber}  = {userAddition} ",)

#elif for Minus
elif mathRequest == "Minus" or mathRequest == "minus" or mathRequest == "2" :
    userMinus = firstNumber - secondNumber
    print(f"{userFirstName}  {firstNumber} Minus {secondNumber}  = {userMinus}")
    
#elif for Multipliction
elif mathRequest == "Multipliction" or mathRequest == "multipliction" or mathRequest == "3" :
    userMultipliction = firstNumber * secondNumber
    print(f"{userFirstName}  {firstNumber} Multiply By {secondNumber} = {userMultipliction}")

#elif for Division
elif mathRequest == "Division" or mathRequest == "division" or mathRequest == "4" :
    userDivision = firstNumber / secondNumber 
    print(f"{userFirstName} {firstNumber} Divided By {secondNumber} = {userDivision} ")
    
#elif for Exponentiation
elif mathRequest == "Exponentiation"  or mathRequest == "exponentiation" or mathRequest == "5" :
    userExponentiation = firstNumber ** secondNumber
    print(f"{userFirstName} {firstNumber} Raised to The Power of {secondNumber} = {userExponentiation}  ")
    
#elif for Modulus
elif mathRequest == "Modulus" or mathRequest == "modulus" or mathRequest == "6" :
    userModulus = firstNumber % secondNumber
    print(f"{userFirstName}  The Remainder of {firstNumber} Divided by {secondNumber} = {userModulus} ") 
    
#elif for Exit
elif mathRequest == "Exit" or mathRequest == "exit" or mathRequest == "7" :
    print(f"Hope To See You Again {userFirstName} {userFamilyName}")
    
#else 
else :
    print(f"{userFirstName} Pls Enter A Option From The Menu")    

     




