from flask import request, jsonify
from models.schemas.roleSchema import role_schema, roles_schema
from services import roleService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required,admin_required


def save(): #name the controller will always be the same as the service function

    try:
        #try to validate the incoming data, and deserialize
        role_data = role_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    role_saved = roleService.save(role_data)
    return role_schema.jsonify(role_data), 201
