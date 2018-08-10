# -*- coding: utf-8 -*-
"""Base application module. Used to register services (Container)"""
import dependency_injector.providers as providers
from falcon import API

from api.application.environments.config import CONFIG
from api.application.middlewares import database
from api.application.services.service_register import ServiceRegister


APP_MIDDLEWARE = [
    database.DatabaseMiddleware()
]


class Application(object):
    def __init__(self):
        self.app_config = providers.Singleton(CONFIG)
        self.api = API(middleware=APP_MIDDLEWARE)
        self.start()

    def start(self):
        ServiceRegister.register_services(self.api)


app = Application()
app.api.req_options.auto_parse_form_urlencoded = True
