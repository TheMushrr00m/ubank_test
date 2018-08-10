# -*- coding: utf-8 -*-
from peewee import Model

from api.infraestructure.database import database


class BaseModel(Model):
    class Meta:
        database = database.db
