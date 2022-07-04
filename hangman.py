import imp


import os
os.system("cls")
import random


superHeroes = ["Ironman","Thor","DeadPool","Antman","Avengers","Hulk","BlackPanther","SpiderMan","Venom","Batman","Superman","WonderWoman","DoctorStrange"]
print(superHeroes)
gamecontinue = "Y"
hangMan = list(random.choice(superHeroes).lower())
print(hangMan)
guessHangman = ["_"]*len(hangMan)
print("\nYou Have to Try to Guess  Name of a SuperHero\n")
print(guessHangman)

while guessHangman.count("_") > 0 :
    
    userGuess = input("Pls enter a Letter : ")
    for i in range(len(hangMan)) :
        if userGuess == hangMan[i] :
            guessHangman[i] = userGuess
            print(guessHangman)
        
        elif userGuess != hangMan[i] :
            print("\nThe Letter You Typed isnn\'t in The Word Try Again\n")
            break
        




