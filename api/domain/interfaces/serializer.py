# -*- coding: utf-8 -*-
from marshmallow import Schema, fields


class BaseSerializer(Schema):
    id = fields.Int(dump_only=True)
