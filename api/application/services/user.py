# -*- coding: utf-8 -*-
import falcon
import json
from api.application.interfaces.item_resource import IResourceItem
from api.application.interfaces.collection_resource import IResourceCollection
from api.domain.serializers.user import UserSchema
from api.domain.repositories.user import UserRepository
from api.application.utils.schemas import deserialize, serialize

user_schema = UserSchema()
many_users_schema = UserSchema(many=True)


class UserResource(IResourceItem, UserRepository):

    def on_get(self, req, resp, obj_id):
        obj = self.get_object(obj_id)
        sr_obj = serialize(obj, user_schema)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(sr_obj.data)
        return resp

    def on_patch(self, req, resp, obj_id):
        patch_data = req.media
        user, errors = deserialize(patch_data, user_schema)
        if errors or not user:
            resp.body = json.dumps(errors)
        elif user:
            updated = self.update_object(user, obj_id)
            resp.body = json.dumps({'updated_rows': updated})
        else:
            resp.body = json.dumps({'updated_rows': 0})
        resp.status = falcon.HTTP_200
        return resp

    def on_delete(self, req, resp, obj_id):
        deleted = self.delete_object(obj_id)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'deleted_rows': deleted})
        return resp


class UserCollection(IResourceCollection, UserRepository):

    def on_get(self, req, resp):
        obj_list = self.get_object_list()
        sr_data = serialize(obj_list, many_users_schema)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(sr_data.data)
        return resp

    def on_post(self, req, resp):
        post_data = req.media
        data, errors = deserialize(post_data, user_schema)
        if errors or not data:
            resp.status = falcon.HTTP_422
            resp.body = json.dumps(errors)
            return resp
        elif data:
            user = self.create_object(data)
            sr_data = serialize(user, user_schema)
            resp.status = falcon.HTTP_201
            resp.body = json.dumps(sr_data.data)
            return resp
