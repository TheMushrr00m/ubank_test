# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class IRepository(metaclass=ABCMeta):

    @abstractmethod
    def create_object(self, data):
        pass

    @abstractmethod
    def get_object(self, obj_id):
        pass

    @abstractmethod
    def get_object_list(self, query=None):
        pass

    @abstractmethod
    def update_object(self, data, obj_id):
        pass

    @abstractmethod
    def delete_object(self, obj_id):
        pass
