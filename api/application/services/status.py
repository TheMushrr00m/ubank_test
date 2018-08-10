# -*- coding: utf-8 -*-
import falcon
import json


class StatusService(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'status': 'Running correctly'})
        return resp
