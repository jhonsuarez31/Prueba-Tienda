# -- coding: utf-8 --

# Import installed packages
from marshmallow import fields
from marshmallow import Schema


class BaseSchema(Schema):
    def _init_(self, strict=True, **kwargs):
        super(Schema, self)._init_(strict=strict, **kwargs)

    id = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()