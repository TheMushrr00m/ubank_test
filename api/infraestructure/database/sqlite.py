# -*- coding: utf-8 -*-
import dependency_injector.providers as providers
from peewee import SqliteDatabase

from api.application.environments.config import CONFIG


class Database(object):
    def __init__(self, path):
        self.app_config = providers.Singleton(CONFIG)
        self.db = SqliteDatabase(path)
