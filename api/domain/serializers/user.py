# -*- coding: utf-8 -*-
from marshmallow import fields, validate
from api.domain.interfaces.serializer import BaseSerializer


class UserSchema(BaseSerializer):
    name = fields.Str()
    email = fields.Str(validate=validate.Email(error="Not a valid email address"))
    description = fields.Str()
    active = fields.Bool()
    age = fields.Int()
    some_date = fields.Date()
    some_datetime = fields.DateTime()  # "2018-08-09T21:59:00.019077+00:00"
