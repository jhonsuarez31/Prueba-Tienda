# -- coding: utf-8 --

# Import installed packages
from marshmallow import fields
from .base import BaseSchema


class UserSchema(BaseSchema):
    email = fields.Email()
    name = fields.Str()