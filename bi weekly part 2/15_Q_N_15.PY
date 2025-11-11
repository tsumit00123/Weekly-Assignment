"""
15. Write a program to create a number guessing game for the user. The program should ask the user to input a number. The program specifications are as mentioned below.
I.The program should generate a random number for the answer.
II.The program should prompt the user for a number input.
III.The program should provide the feedback to the user after each guesses (e.g. “Too high”, “Too low” or “Correct number”).
IV.The program should check the user input for 5 times and allow the users to guess for at most 5 times if their input don’t match the answer number.
V.If the user is not able to guess the answer within 5 times, the program should display “Game Over” message and exit.
"""

import random
print("Welcome to my number guessing game", chr(128587))
print()
print("------------------------------------------------")
while True:
    Range=input("Enter the number between 0 to: ")
    if Range.isdigit():
        Range=int(Range)
        if Range<=0:
            print("Please enter the number greater than 0 next time")
            continue

        else:
            print("You are good to play the game")

    else:
        print("Please enter integer not letter.")
        continue

    print("-------------------------------------------------")
    Computer_generated=random.randint(0,Range)
    MAX_LIMIT=6
    Guesses=0

    while Guesses<MAX_LIMIT:
        user_guess=input(f"Make a guess between 0-{Range}: ")
        if user_guess.isdigit():
            user_guess=int(user_guess)
            if user_guess>Range:
                print(f"Please make a guess between 0-{Range}")
                continue

            Guesses+=1
            if user_guess==Computer_generated:
                print("You got it! ",chr(128079))
                break

            elif user_guess>Computer_generated:
                print(f" Too High! Try lower than {user_guess}")

            else:
                print(f"Too Low! Try higher than {user_guess}")

        else:
            print("Next time enter Integer not letter")
           
            

    if user_guess<MAX_LIMIT and user_guess!=Computer_generated:
        print("You hit maximum limit. Game Over")
        print()
        print(f"The correct guess was {Computer_generated}")

    else:
        print(f"You got it into {Guesses} guesses")

    print("-----------------------------------------------------")

    print("Do you want to play again")
    play_again=input("press enter to play game or q to quite the game: ").upper()
    if play_again=="Q":
        print("Thank you for play the game. Goodbye")
        break
    else:
        print("Starting a new game!")



    



    