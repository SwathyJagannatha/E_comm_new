from flask import request, jsonify
from models.schemas.customeraccountSchema import customeraccnt_schema, customeraccnts_schema
from services import customeraccountService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required,admin_required
from limiter import limiter

def save(): #name the controller will always be the same as the service function

    try:
        #try to validate the incoming data, and deserialize
        customeraccnt_data = customeraccnt_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400

    response,status = customeraccountService.save(customeraccnt_data)

    if status != 201:
        return jsonify(response),status 
    return customeraccnt_schema.jsonify(response), status

    
@cache.cached(timeout=60)
#@admin_required
def find_all():
    response,status = customeraccountService.find_all()

    if status!=201:
        return jsonify(response),status 
    return customeraccnts_schema.jsonify(response),status
    
@limiter.limit("5 per minute")
def update_customeraccnt(id): #name the controller will always be the same as the service function
    try:
        data = request.json
        #try to validate the incoming data, and deserialize
        response,status=customeraccountService.update_customeraccnt(id,data)

        if status != 201:
            return jsonify(response),status
        return customeraccnt_schema.jsonify(response), status
        
    except ValidationError as e:
        return jsonify(e.messages), 400
    
@limiter.limit("5 per minute")
def delete_customeraccnt(id):

    response,status =customeraccountService.delete_customeraccnt(id)
    if status!=201:
       return jsonify(response),status
    else:
        return customeraccnts_schema.jsonify(response),status

