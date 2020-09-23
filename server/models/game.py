#!/usr/bin/env python3

"""
game.py

SQLAlchemy class to store information about a high/low online game

Author: Dr. Andreas Janzen, janzen@gmx.net
Date: 2020-09-11
"""

import datetime
import sqlalchemy
import uuid

from models.model_base import ModelBase


class Game(ModelBase):
    __tablename__ = "games"

    game_id = sqlalchemy.Column(sqlalchemy.String, primary_key=True,
                           default=uuid.uuid4())
    player_id = sqlalchemy.Column(sqlalchemy.Integer)
    game_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                  default=datetime.datetime.now)
    secret_number = sqlalchemy.Column(sqlalchemy.Integer)
    guesses = sqlalchemy.Column(sqlalchemy.String)
