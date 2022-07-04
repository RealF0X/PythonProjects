import os
import random
os.system('cls')
Playagain = "y" 
while Playagain == "y" :
    pcListofChoice = ["Rock","Paper","Scissors"]
    pcChoice = random.choice(pcListofChoice)
    
    makeYourChoice = input(f" PLs Enter Your Choice Between \n 1) Rock  \n 2) Paper \n 3) Scissors : ")

    if makeYourChoice == "Rock" or makeYourChoice == "rock"  or makeYourChoice == "1" :
        print()
        if pcChoice == "Rock" :
            print(f"\n Draw \n Pc also Chose Rock so Its a Draw\n")
        elif pcChoice == "Paper":
            print(f"\n Pc Won \n Because Pc Chose Paper\n")
        elif pcChoice == "Scissors" :
            print(f"\n You Won \n Because Pc Chose Scissors\n")            

    if makeYourChoice == "Paper" or makeYourChoice == "paper" or makeYourChoice == "2":
        if  pcChoice == "Rock" :
            print(f"\n You Won \n Because Pc Chose Rock\n")            
        elif pcChoice == "Paper":
            print(f"\n Draw   \n Pc also Chose Paper so Its a Draw\n ")
        elif pcChoice == "Scissors" :  
            print(f"\n Pc Won \n Because Pc Chose Scissors\n")

    if makeYourChoice == "Scissors" or makeYourChoice == "scissors" or makeYourChoice == "3":
        if  pcChoice == "Rock" :
            print(f"\n Pc Won \n Because Pc Chose Rock\n")                   
        elif pcChoice == "Paper": 
            print(f"\n You Won \n Because Pc Chose Paper\n") 
        elif pcChoice == "Scissors":
            print(f"\n Draw   \n Pc also Chose Scissors so Its a Draw\n ")

    else :
        print("Pls Enter a Valid Choice")
    
    Playagain = input("Do You Want To Play Again? (Y/N)")