#!/usr/bin/env python3

"""
player.py

SQLAlchemy model to store information about players

Author: Dr. Andreas Janzen, janzen@gmx.net
Date: 2020-09-12
"""

import datetime
import sqlalchemy

from models.model_base import ModelBase


class Player(ModelBase):
    __tablename__ = "players"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
            autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    created = sqlalchemy.Column(sqlalchemy.DateTime,
            default=datetime.datetime.now)

