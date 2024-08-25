# E-Commerce API with CI/CD Pipeline

Welcome to the E-Commerce API project! This application is built using Flask, with a focus on managing various aspects of an e-commerce platform, including customers, products, orders, roles, and customer accounts. The project also incorporates a Continuous Integration and Continuous Deployment (CI/CD) pipeline for seamless development and deployment.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [Role Management](#role-management)
  - [Customer Management](#customer-management)
  - [Customer Account Management](#customer-account-management)
  - [Order Management](#order-management)
  - [Product Management](#product-management)
- [CI/CD Pipeline](#cicd-pipeline)
- [Database Configuration](#database-configuration)
- [Testing](#testing)
- [Deployment](#deployment)
- [Swagger Documentation](#swagger-documentation)
- [GitHub Repository](#github-repository)
- [Project Communication](#project-communication)
- [Submission](#submission)

## Project Overview

This project serves as a comprehensive example of a Flask-based API for an e-commerce platform, including functionality for managing customers, products, orders, roles, and customer accounts. The API is deployed on Render, with a PostgreSQL database for data storage. The CI/CD pipeline, set up with GitHub Actions, automates the build, test, and deployment processes.

## Features

- **Role Management**: Create, retrieve, update, and delete roles.
- **Customer Management**: Manage customers, including registration, login, updating, and deletion.
- **Customer Account Management**: Handle customer account details with CRUD operations.
- **Order Management**: Manage orders, including creation, retrieval by ID or customer, updating, and deletion.
- **Product Management**: Manage product details, including creation, updating, deletion, and search functionality.

## Installation

1. Clone the repository:
2. 
   git clone https://github.com/SwathyJagannatha/E_comm_new.git
   cd E_comm_new

3. Create a Virtual Environment:

python -m venv venv
source venv/bin/activate

3. Install Dependencies:

pip install -r requirements.txt

4. Run the Application:

flask run

5. Run Tests:

python -m unittest discover -s tests

6. API Documentation

The API documentation is generated using Swagger and can be accessed at /swagger.

GitHub Actions Workflow:

The CI/CD pipeline is defined in the main.yml file located in the .github/workflows directory.

### Workflow Overview

- **Build**: 
  - Set up Python environment.
  - Install dependencies.
  - Print debugging information.

- **Test**:
  - Run unit tests using `unittest` and `pytest`.

- **Deploy**:
  - Deploy the application to Render after successful tests.
  
API Endpoints

Role Management

POST /roles/: Create a new role.
GET /roles/: Retrieve all roles.
PUT /roles/{id}: Update a role by ID.
DELETE /roles/{id}: Delete a role by ID.

Customer Management

POST /customers/: Register a new customer.
GET /customers/: Retrieve all customers.
POST /customers/login: Login a customer.
PUT /customers/{id}: Update a customer by ID.
DELETE /customers/{id}: Delete a customer by ID.

Customer Account Management

POST /customeraccnt/: Create a new customer account.
GET /customeraccnt/: Retrieve all customer accounts.
PUT /customeraccnt/{id}: Update a customer account by ID.
DELETE /customeraccnt/{id}: Delete a customer account by ID.

Order Management

POST /orders/: Create a new order.
GET /orders/: Retrieve all orders.
GET /orders/{id}: Retrieve an order by ID.
GET /orders/customer/{id}: Retrieve orders by customer ID.
POST /orders/customer/email: Retrieve orders by customer email.
PUT /orders/{id}: Update an order by ID.
DELETE /orders/{id}: Delete an order by ID.

Product Management

POST /products/: Create a new product.
GET /products/: Retrieve all products.
GET /products/search: Search for products.
PUT /products/{id}: Update a product by ID.
DELETE /products/{id}: Delete a product by ID.

CI/CD Pipeline

The CI/CD pipeline is set up using GitHub Actions to automate the process of building, testing, and deploying the application. The pipeline includes the following stages:

Build: Checks out the code, sets up the Python environment, and installs dependencies.
Test: Runs unit tests using unittest and pytest.
Deploy: Deploys the application to Render, triggered only after successful tests.
The pipeline configuration is defined in the main.yml file located in the .github/workflows directory.

Database Configuration

This project uses PostgreSQL as the database, hosted on Render. The database connection is configured using the psycopg2 library. Ensure the necessary environment variables are set for the database connection.

Testing

Unit tests are implemented using unittest and pytest. The tests cover various aspects of the application, including API endpoints and business logic.

Run the tests using the following command:

python -m unittest discover -s tests -p 'test_m*.py

Deployment

The application is deployed on Render, a cloud platform for hosting web applications and databases. The deployment process is automated via the CI/CD pipeline configured in GitHub Actions.

## Deployment

The application is deployed on Render and can be accessed at: [E-Commerce API on Render](https://e-comm-new-1.onrender.com)


Swagger Documentation

Swagger is integrated into the API to provide comprehensive documentation of the endpoints. This documentation can be accessed through the Swagger UI, allowing for easy interaction with the API.

GitHub Repository
The project's source code is hosted on GitHub. You can find the repository here: E-Comm New Repository.