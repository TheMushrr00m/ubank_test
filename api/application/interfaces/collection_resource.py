# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class IResourceCollection(metaclass=ABCMeta):
    """Collection of Resources abstract class, inherits from BaseClass
       POST Ignores query parameters.
       GET can work with and without query parameters.
       query params support advanced comparison like gt, gte, lt and lte
       Examples: '/residences/?opens_at__lt=08:30:00',
                '/residences/?name__startswith=kf'
    """
    @abstractmethod
    def on_get(self, req, resp):
        pass

    @abstractmethod
    def on_post(self, req, resp):
        pass
