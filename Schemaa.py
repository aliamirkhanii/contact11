from marshmallow import Schema, fields


class MySchema(Schema):
    firstname = fields.String(required=True, description='First Name')
    lastname = fields.String(required=True, description='Last Name')
    phone_number = fields.Number(required=True, validate=lambda s: len(s) == 11 and s.isdigit(),
                                 description='Phone Number(11)')
