#!/usr/bin/env python3

"""
game.py

Contains the main game loop of the high/low web app, as well as functions to
support the main loop, except for the database access

Author: Dr. Andreas Janzen, janzen@gmx.net
Date: 2020-09-13
"""

import db_services


def game_loop():
    print("In game loop")

    AJ = db_services.create_player("Andreas Janzen")
    game = db_services.new_game()


if __name__ == "__main__":
    game_loop()
