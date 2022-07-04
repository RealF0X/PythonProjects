import os
os.system("cls")
import random

playAgain = "Y"
while playAgain == "Y" :
    superHeroes = ["Ironman","Thor","DeadPool","Antman","Avengers","Hulk","BlackPanther","SpiderMan","Venom","Batman","Superman","WonderWoman","DoctorStrange"]
    gamecontinue = "Y"
    hangMan = list(random.choice(superHeroes).lower())
    guessHangman = ["_"]*len(hangMan)
    print("\nYou Have to Try to Guess  Name of a SuperHero\n")
    print(guessHangman)


    while guessHangman.count("_") > 0 :
        
        userGuess = input("Pls enter a Letter : ")
        for i in range(len(hangMan)) :
            if userGuess == hangMan[i] :
                guessHangman[i] = userGuess
                print(guessHangman)
                
    playAgain = input("Do You Want To Play Again?(Y/N) ").upper()        
        



