#!/usr/bin/env python3

"""
game.py

Contains the main game loop of the high/low web app, as well as functions to
support the main loop, except for the database access

Author: Dr. Andreas Janzen, janzen@gmx.net
Date: 2020-09-13
"""

import db_services
import random
import sys


def game_intro():
    print("\n"*3 + "="*26)
    print("===" + " "*20 + "===")
    print("===  GUESS THE NUMBER  ===")
    print("===" + " "*20 + "===")
    print("="*26)

    print("(1) Start new game")
    print("(2) View stored games")
    print("(3) Quit the game")

    while True:
        action = input("\nWhat would you like to do? > ")

        if action == "1":
            game_loop()
        elif action == "2":
            view_stored_games()
        elif action == "3":
            print("\nGood bye!\n")
            sys.exit()
        break


def game_loop():
    print("\n\nStarting a new game...")
    print("Please guess the secret number in the range 1...100!")

    secret_number = random.randint(1,100)
    # print(f"The secret number is {secret_number}.")

    while True:
        num = input("\nPlease enter your guess > ")
        try:
            guess = int(num)
        except:
            print("That was not a proper number. Try again!")
            continue
        if guess < secret_number:
            print("Your guess was too low!")
        elif guess > secret_number:
            print("Your guess was too high!")
        else:
            print("\n\n" + "*"*47)
            print("***" + " "*41 + "***")
            print("***  Yeah! Congratulations, you nailed it!  ***")
            print("***" + " "*41 + "***")
            print("*"*47)
            break


if __name__ == "__main__":
    while True:
        game_intro()
