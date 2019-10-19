#guessing game
#10/16/2019
#Matt Landale

animal = 'lion'


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

    

def main():
    while continue_game():
        continue_game()

def continue_game():

    answer = input("Do you wish to continue?: ")
#Issue S - Must be Uppercase "Q"
    if answer == "q":
        print("You have chosen to continue on")
        return True
    else:
        print("You have chosen to quit this program")
        return False

if __name__ == "__main__":
    main()



