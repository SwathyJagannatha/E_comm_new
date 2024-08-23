from models.role import Role
#from models.orderProduct import order_product
from database import db
from sqlalchemy import select,delete

def save(role_data):
    role_name = role_data.get('role_name')

    if not role_name:
        return {
            "status": "fail",
            "message": "Missing the required field,role name"
        }
    
    existing_role_query = select(Role).where(Role.role_name == role_name)
    existing_role = db.session.execute(existing_role_query).scalar_one_or_none()

    if existing_role:
        return{
            "status":"fail",
            "message":"Role table already has this role name entry"
        }
    try:
        new_role = Role(role_name = role_data["role_name"])

        db.session.add(new_role)
        db.session.commit()
        db.session.refresh(new_role)

        return{
            "status":"sucess",
            "message":"New Role successfully added",
            "data": new_role
        }
    
    except Exception as e:
        db.session.rollback()
        return{
            "status":"fail",
            "message": f"Failed to create new role:{str(e)}"
        }
    

# def find_all():
#     query = select(Product)
#     all_products = db.session.execute(query).scalars().all()
#     return all_products

# def search_product(search_term):
#     query = select(Product).where(Product.name.like(f'%{search_term}%'))
#     search_products = db.session.execute(query).scalars().all()
#     return search_products

# def delete_product(id):
#     query = select(Product).where(Product.id == id)
#     prod = db.session.execute(query).scalar()

#     if prod:
#         # Delete all associations from the order_product table where product_id matches
#         db.session.execute(
#             delete(order_product).where(order_product.c.product_id == id)
#         )

#         db.session.delete(prod)
#         db.session.commit()
#         return prod
#     else:
#         return None
    
# def update_product(id,data):
#     try:
#         query = select(Product).where(Product.id == id)
#         prod = db.session.execute(query).scalar()
#         prod.name = data.get("name",prod.name)
#         prod.price = data.get("price",prod.price)

#         db.session.commit()
#         return prod
#     except:
#         return None
    




    
