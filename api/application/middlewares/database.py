#! -*- coding: utf-8 -*-
from api.infraestructure.database import database


class DatabaseMiddleware(object):
    def process_request(self, req, resp):
        """Ensure a separate connection for each thread"""
        if req is not None:
            req.db = database.db
            req.db.connect()

    def process_response(self, req, resp, resource, req_succeeded):
        """Close db connection"""
        if hasattr(req, 'db'):
            if not req.db.is_closed():
                req.db.close()
