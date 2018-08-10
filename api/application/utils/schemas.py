# -*- coding: utf-8 -*-
"""Schema Utilities"""
from marshmallow import ValidationError


def serialize(data, schema):
    """Serializes the ORM objects using its corresponding schema
        to be json encoded.

        Args:
            data: ORM Object or List of objects depending
                on the instance schema if many == True or not
            schema: A Schema Object that it's used to dump information of the ORM object.
        Returns:
            sr_data: serialized data to be encoded
    """
    sr_data = schema.dump(data)
    return sr_data


def deserialize(json_input, schema, **kwargs):
    """Deserializes and validates the json_input.

       Args:
           json_input: raw input json.
           schema: A Schema Object that it's used to dump information of the ORM object.
           many(optional): bool to control over how to deserialize
                           regardless of how the schema is initiated (Bulk insertion).
       Returns:
           clean_data: valid Python dict that complies to the schema.
           errors: marshmallow object containing errors in json_input.
    """
    many = kwargs.get('many', None)
    try:
        if many is None:
            clean_data, errors = schema.load(json_input)
        else:
            clean_data, errors = schema.load(json_input, many=many)
        return clean_data, errors
    except ValidationError:
        return ValidationError("Data can't be converted")
