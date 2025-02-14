import random
import os


codes = ("0","1","2","3","4","5","6","7","8","9")
code = random.choice(codes)

os.system("cls" if os.name == "nt" else "clear")
print("Welcome to GuessTheCode!\nThe rules are simple, there are 9 possible combinations from 0 to 9!\nTry brute forcing, messing with the code, or guessing one by one. Just have fun!\n             ~MIT License ~Project created by https://github.com/untitled-guy")
input("\n\n\nPress enter to start. . .")
while True:
    os.system("cls" if os.name == "nt" else "clear")
    guess = input("Code:")
    if guess == code:
        print("You won!")
        input("Press enter to exit!. . .")
        os.system("cls" if os.name == "nt" else "clear")
        break
    else:
        print("You lost!")
        input("Press enter to try again!. . .")
        os.system("cls" if os.name == "nt" else "clear")
        
