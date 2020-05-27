

UserGuess = input ("What is your guess")

from random import randrange
Num =(randrange(10))
#print(Num)

UserGuess = int(UserGuess)
Num = int(Num)

if UserGuess > Num:
    print("Too high guess lower")
elif UserGuess < Num:
    print("Too low guess higher") 
