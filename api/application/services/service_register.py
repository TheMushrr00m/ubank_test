# -*- coding: utf-8 -*-
from api.application.services import status, user


class ServiceRegister(object):
    @staticmethod
    def register_services(api):
        api.add_route('/', status.StatusService())
        api.add_route('/users', user.UserCollection())
        api.add_route('/users/{obj_id:int}', user.UserResource())
