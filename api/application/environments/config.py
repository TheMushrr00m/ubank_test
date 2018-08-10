#! -*- coding: utf-8 -*-
import os


class BaseConfig(object):
    APP_DB_ENGINE = os.environ.get('APP_DB_ENGINE', 'sqlite')
    APP_DB_NAME = os.environ.get('APP_DB_NAME', 'Ubank.db')


CONFIG = BaseConfig
