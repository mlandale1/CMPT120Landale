#guessing game
#10/16/2019
#Matt Landale

import random

animal = "lion"

print("Lets play a guessing game!")
            
while True:
        print("I am thinking of a random animal. Try to guess the animal!")
        prompt = input("Guess: ")
        animal = "lion"

        if prompt == animal:
            print("Correct!")
            break
        else:
            print("Incorrect!")
            

