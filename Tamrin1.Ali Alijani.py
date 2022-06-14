#User Name 
from ast import alias
from traceback import print_tb


userFirstName = input(" Pls Enter Your First Name : ")
userFamilyName = input("Pls Enter Your Family Name :  ")

#Welcome Message
print(f" \n Welcome to This App {userFirstName} {userFamilyName} \n ")

#Menu
print("  ➕ Addition ➡️   + \n  ➖ Minus ➡️   - \n  ❌ Multipliction ➡️    * \n  ➗ division ➡️    /  \n  💪 Exponentiation ➡️    ** \n  👌 Modulus ➡️   %  \n  👋 Exit ➡️   Exit \n")

#Asking for User Numbers & Math operator 
firstNumber = int(input(f"{userFirstName}   pls Enter Your First number  : "))
secondNumber = int(input(f"{userFirstName}  pls Enter Your Second number : "))
mathRequest = input("Which Option From The Menu Would You Like To Choose (You Can Select The Name of Math Action From The Menu Starting with Lower Case) :  ")


#if 
if  mathRequest == "addition"  :
    userAddition = firstNumber + secondNumber
    print(f"{userFirstName} The Addition of {firstNumber} & {secondNumber}  = {userAddition} ",)

#elif for Minus
elif  mathRequest == "minus"  :
    userMinus = firstNumber - secondNumber
    print(f"{userFirstName}  {firstNumber} Minus {secondNumber}  = {userMinus}")
    
#elif for Multipliction
elif  mathRequest == "multipliction"  :
    userMultipliction = firstNumber * secondNumber
    print(f"{userFirstName}  {firstNumber} Multiply By {secondNumber} = {userMultipliction}")

#elif for Division
elif  mathRequest == "division"  :
    userDivision = firstNumber / secondNumber 
    print(f"{userFirstName} {firstNumber} Divided By {secondNumber} = {userDivision} ")
    
#elif for Exponentiation
elif mathRequest == "exponentiation"  :
    userExponentiation = firstNumber ** secondNumber
    print(f"{userFirstName} {firstNumber} Raised to The Power of {secondNumber} = {userExponentiation}  ")
    
#elif for Modulus
elif  mathRequest == "modulus"  :
    userModulus = firstNumber % secondNumber
    print(f"{userFirstName}  The Remainder of {firstNumber} Divided by {secondNumber} = {userModulus} ") 
    
#elif for Exit
elif  mathRequest == "exit"  :
    print(f"Hope To See You Again {userFirstName} {userFamilyName}")
    
    
#else 
else :
    print(f"{userFirstName} Pls Enter A Option From The Menu")
        

     




