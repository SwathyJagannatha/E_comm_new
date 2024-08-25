import unittest
from faker import Faker
from app import create_app, blueprint_config, db

class testApi(unittest.TestCase):
 def setUp(self):
        # Set up the app and the app context
        self.app = create_app('DevelopmentConfig')
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
        
        with self.app.app_context():
           db.drop_all() 
           db.create_all()  # Create the database tables

           from models.role import Role
           db.session.add(Role(role_name="Admin"))
           db.session.add(Role(role_name="User"))
           db.session.commit()
        self.client = self.app.test_client()
        self.fake = Faker()

 def test_customer(self):
        # Generate fake customer data
        name = self.fake.name()
        email = self.fake.email()
        username = self.fake.user_name()
        password = self.fake.password()
        role_id = self.fake.random_int(min=1, max=2)
        payload = {
            "id":1,
            "name": name,
            "email": email,
            "phone": self.fake.phone_number(),
            "username": username,
            "password": password,
            "role_id": role_id
        }

        # Send a POST request to create a new customer
        response = self.client.post('/customers/', json=payload)

        # Print out response content and status for debugging
        print(response)
        print(response.status_code)
        print(response.data)

        # Check the response status code
        self.assertEqual(response.status_code, 201)

        # Now try to parse the JSON response
        data = response.get_json()

        # Check if the response contains JSON data
        self.assertIsNotNone(data, "Response did not contain JSON data")

        self.assertEqual(data['name'], name)
        self.assertEqual(data['email'], email)
    
 def test_customeraccnt(self):
    # Generate fake customer data
    id = 2
    name = self.fake.name()
    email = self.fake.email()
    username = self.fake.user_name()
    password = self.fake.password()
    role_id = self.fake.random_int(min=1, max=2)
    payload = {
        "id": id,
        "name": name,
        "email": email,
        "phone": self.fake.phone_number(),
        "username": username,
        "password": password,
        "role_id": role_id
    }

    # Send a POST request to create a new customer
    response = self.client.post('/customers/', json=payload)

    if response.status_code != 201:
        print("Failed to create customer:", response.status_code, response.data)
        self.fail("Customer creation failed in test setup")
    else:
        print("Customer creation successful:")
        print(response.data)

    # Retrieve the created customer's ID from the response
    created_customer_data = response.get_json()
    customer_id = created_customer_data['id']  # Make sure to use the correct key

    # Ensure that the customer ID is correct
    print("Using customer_id:", customer_id)

    payload = {
        "username": self.fake.user_name(),
        "password": self.fake.password(),
        "customer_id": customer_id
    }

    # Send a POST request to create a new customer account
    response = self.client.post('/customeraccnt/', json=payload)

    # Print out response content and status for debugging
    print(response)
    print(response.status_code)
    print(response.data)

    # Check the response status code
    if response.status_code != 201:
        print("Failed to create customeraccount:", response.status_code, response.data)
        #self.fail("Customeraccount creation failed in test setup")

    # Now try to parse the JSON response
    data = response.get_json()

    # Check if the response contains JSON data
    self.assertIsNotNone(data, "Response did not contain JSON data")

    # self.assertEqual(data['username'], payload["username"])
    # self.assertEqual(data['password'], payload["password"])

 def test_order(self):
    # Manually insert a customer with a specific id
    with self.app.app_context():
        from models.customer import Customer
        customer = Customer(
            id=10,  # Setting the id explicitly to 10
            name=self.fake.name(),
            email=self.fake.email(),
            phone=self.fake.phone_number(),
            username=self.fake.user_name(),
            password=self.fake.password(),
            role_id=self.fake.random_int(min=1, max=2)
        )
        db.session.add(customer)
        db.session.commit()

    # order payload
    payload = {
        "customer_id": 10,  # Using the specific id of the customer we just inserted
        "date": self.fake.date(),
        "products": [
            {"id": self.fake.random_number(1, 5), "name": self.fake.name(), "price": self.fake.random_number(1, 40)},
            {"id": self.fake.random_number(1, 5), "name": self.fake.name(), "price": self.fake.random_number(1, 40)}
        ]
    }

    # Send a POST request to create a new order
    response = self.client.post('/orders/', json=payload)

    # Print out response content and status for debugging
    print(response)
    print(response.status_code)
    print(response.data)

    # Check the response status code
    self.assertEqual(response.status_code, 201)

    # Now try to parse the JSON response
    data = response.get_json()

    # Additional assertions can be added as needed

if __name__ == '__main__':
    unittest.main()