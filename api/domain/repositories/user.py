# -*- coding: utf-8 -*-
import falcon
from api.domain.interfaces.repository import IRepository
from api.domain.models.user import User


class UserRepository(IRepository):
    def __init__(self):
        self.model = User

    def create_object(self, data):
        obj = self.model.create(**data)
        return obj

    def get_object(self, obj_id):
        try:
            obj = self.model.get(self.model.id == obj_id)
            if not obj.active:
                raise falcon.HTTPNotFound
        except (self.model.DoesNotExist, ValueError):
            raise falcon.HTTPNotFound
        return obj

    def get_object_list(self, query=None):
        result = self.model.select().where(self.model.active)
        return result

    def update_object(self, data, obj_id):
        try:
            query = self.model.update(**data).where(self.model.id == obj_id)
            updated = query.execute()
        except KeyError:
            return falcon.HTTPBadRequest
        return updated

    def delete_object(self, obj_id):
        query = self.model.delete().where(self.model.id == obj_id)
        deleted = query.execute()
        return deleted
