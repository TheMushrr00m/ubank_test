# -*- coding: utf-8 -*-
from peewee import BooleanField, CharField, DateField, DateTimeField, IntegerField, TextField
from api.domain.interfaces.model import BaseModel


class User(BaseModel):
    name = CharField(max_length=45)
    email = CharField(max_length=45, unique=True)
    description = TextField()
    active = BooleanField(default=True)
    age = IntegerField()
    some_date = DateField(null=True)
    some_datetime = DateTimeField(null=True)
