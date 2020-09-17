#!/usr/bin/env python3

"""
db_services.py

Collection of functions for database communication of the high/low online game

Author: Dr. Andreas Janzen, janzen@gmx.net
Date: 2020-09-11
"""

import os
import sqlalchemy
import sqlalchemy.orm
import uuid

from models.game import Game
from models.model_base import ModelBase
from models.player import Player


DB_FILE = "high_low.sqlite"

__factory = None


# GLOBAL HELPER FUNCTIONS

def global_init():
    global __factory

    base_folder = os.path.dirname(__file__)
    full_file = os.path.join(base_folder, DB_FILE)
    conn_str = "sqlite:///" + full_file

    engine = sqlalchemy.create_engine(conn_str, echo=False)
    ModelBase.metadata.create_all(engine)

    __factory = sqlalchemy.orm.sessionmaker(bind=engine)


def create_session():
    global __factory

    if __factory is None:
        global_init()

    return __factory()


# GAME-RELATED FUNCTIONS

def create_player(name):
    print(f"Creating new player {name}...")
    session = create_session()

    player = session.query(Player).filter(Player.name == name).first()

    if player:
        print(f"\nPlayer already exists: {player.name}")
        return None

    player = Player()
    player.name = name
    session.add(player)
    session.commit()
    session.close

    player = session.query(Player).filter(player.name == name)
    return player


def new_game(player_name):
    # game_id, player_id, game_date, secret_number, guesses
    new_id = uuid.uuid4()
    print(f"Creating new game {new_id}")

    session = create_session()

    game = Game()
    game.game_id = new_id
    game.player = player_name

    session.add(game)
    session.commit()
    session.close()

    game = session.query(Game).filter(game.id == new_id)
    return game


def retrieve_game():
    pass


def store_game():
    pass
