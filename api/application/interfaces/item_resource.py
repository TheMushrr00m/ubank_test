# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class IResourceItem(metaclass=ABCMeta):
    """Single resource abstract class,
       This uses the Falcon event handlers to manage GET, PATCH, DELETE
       POST is not supported here since its a change that affect a Collection.
       Each method expects obj_id to the request uri.
    """

    @abstractmethod
    def on_get(self, req, resp, obj_id):
        pass

    @abstractmethod
    def on_patch(self, req, resp, obj_id):
        pass

    @abstractmethod
    def on_delete(self, req, resp, obj_id):
        pass
