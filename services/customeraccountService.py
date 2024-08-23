from database import db
from models.customer import Customer 
from models.customeraccount import CustomerAccount
from models.order import Order
from sqlalchemy import select
from utils.util import encode_token
from sqlalchemy.orm import joinedload
from flask import jsonify

def save(customeraccount_data):
    
    customer_id = customeraccount_data.get('customer_id')
    username =  customeraccount_data.get('username')
    password = customeraccount_data.get('password')

    customer=db.session.query(Customer).filter_by(id = customer_id).one_or_none()

    if not customer:
        return {
            "status":"fail",
            "message": "Customer id not found"
            },400
    
    # try:
    #     # Fetch the existing CustomerAccount by ID
    #     customer_account = db.session.query(Customer).filter_by(Customer.id == customer_id).one()
    # except Exception:
    #     raise ValueError(f"No CustomerAccount found with ID {customer_id}")

    query = select(CustomerAccount).where(CustomerAccount.username == username)
    username_info=db.session.execute(query).scalar_one_or_none()

    if username_info:
        return {
            "status":"fail",
            "message": "Username already exists in our system"
            },400
    
    new_customeraccnt = CustomerAccount(
        password = customeraccount_data['password'],
        username = customeraccount_data['username'],
        customer_id = customeraccount_data['customer_id']
    )
    try:
        db.session.add(new_customeraccnt)
        db.session.commit()
        db.session.refresh(new_customeraccnt)

        return{
            "message":"Customer account created successfully",
            "status":"success",
            "data": new_customeraccnt
        },201
    
    except Exception as e:
        db.session.rollback()
        return {
            "status": "fail",
            "message": f"Customer account creation failed: {str(e)}"
        }, 500

def find_all():
    query = select(CustomerAccount)
    all_customeraccnts = db.session.execute(query).scalars().all()
    return all_customeraccnts

def delete_customeraccnt(id):
    if not id:
        print("No ID provided")
        return jsonify({
            "status": "fail",
            "message": "Please provide a customer account id"
        }), 400

    try:
        print(f"Looking for customer account with id: {id}")
        # Query to find the customer account by id
        query = select(CustomerAccount).options(joinedload(CustomerAccount.customer)).where(CustomerAccount.id == id)
        customeraccnt = db.session.execute(query).scalar_one_or_none()

        if not customeraccnt:
            print(f"Customer account with id {id} does not exist")
            return jsonify({
                "status": "fail",
                "message": "Customer account does not exist"
            }), 404

        # If found, delete the customer account
        db.session.delete(customeraccnt)
        db.session.commit()

        print(f"Customer account with id {id} deleted successfully")
        
        return jsonify({
            "message": "Customer account deleted successfully",
            "status": "success",
            "data": {
                "id": customeraccnt.id,
                "username": customeraccnt.username,
                "customer_id": customeraccnt.customer_id
            }
        }), 200

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {str(e)}")
        return jsonify({
            "status": "fail",
            "message": "An error occurred while trying to delete the customer account"
        }), 500

def update_customeraccnt(id,data):
    try:
        query = select(CustomerAccount).where(CustomerAccount.id == id)
        customer=db.session.execute(query).scalar()

        if not customer:
            return {
                "status":"failed",
                "message":"Customer with that id doesnt exist"
            },404
        
        customer.username = data.get("username",customer.username)
        customer.password = data.get("password", customer.password)
        customer.customer_id = data.get("customer_id",customer.customer_id)
        
        db.session.commit()
        db.session.refresh(customer)
        return{
            "mesage":"success",
            "data": customer
        }
    except Exception as e:
         print(f"Exception occured: {e}")

         return {
            "status": "fail",
            "message": "Error occured while updating the Customer account!!"
        }, 404
