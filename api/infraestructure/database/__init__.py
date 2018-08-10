# -*- coding: utf-8 -*-
import dependency_injector.providers as providers
from api.infraestructure.database.sqlite import Database
from api.application.environments.config import CONFIG


app_config = providers.Singleton(CONFIG)
database = Database(app_config().APP_DB_NAME)
