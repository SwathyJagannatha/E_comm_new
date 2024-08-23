
from flask import Blueprint,jsonify,request
from controllers.roleController import save

role_blueprint = Blueprint('role_bp',__name__)

role_blueprint.route('/',methods=['POST'])(save)
# customer_blueprint.route('/', methods=['GET'])(find_all)
# # need to add find_all_paginate

# customer_blueprint.route('/login',methods=['POST'])(login)
# customer_blueprint.route('/<int:id>',methods=['DELETE'])(delete_customer)

# customer_blueprint.route('/<int:id>',methods=['PUT'])(update_customer)
