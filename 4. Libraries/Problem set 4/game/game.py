import random
import sys

def main():
    level = input_valid("Level: ")
    guess_me = random.randint(1, level)
    while True:
        my_guess = input_valid("Guess: ")
        if guess_me > my_guess:
            print("Too small!")
        elif guess_me < my_guess:
            print("Too large!")
        else:
            sys.exit("Just right!")


def input_valid (name):
    while True:
        try:
            nr = int(input(f"{name}: "))
            if nr > 0:
                return nr
        except ValueError:
            continue

main ()