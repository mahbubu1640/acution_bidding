# Auction Bidding App

Welcome to the Auction Bidding App, a Django-based web application for managing auctions and user authentication.

## Prerequisites

Before running the project, make sure you have the following prerequisites installed on your system:

- Python (3.x)
- Django
- Django Rest Framework
- Django Rest Framework Simple JWT

You can install these dependencies using pip:
cmd :
pip install django djangorestframework 
pip install djangorestframework-simplejwt

Project Setup
Clone the repository:
git clone https://github.com/yourusername/auction-bidding-app.git
cd auction-bidding-app

Create a virtual environment :
python -m venv venv

Activate the virtual environment:
# On Windows
venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate

Install project dependencies:
pip install -r requirements.txt

Run database migrations:
python manage.py migrate

Create a superuser account for admin access:
python manage.py createsuperuser

Start the development server:
python manage.py runserver
The project should now be running locally at http://localhost:8000/

User Authentication
Users can register, log in, and log out.
User registration requires providing a unique username, email, and password.
User authentication is token-based, and tokens are obtained by logging in.
User Management
Admins can access all user data.
Admin authentication is based on a static API secret key.
Basic CRUD operations (Create, Read, Update, Delete) on users are available.
Auction Management
Admins can perform CRUD operations on auctions using the static API secret key.
Auctions have attributes such as start time, end time, start price, item name, and user ID of the winning bidder.
Normal users can view ongoing auctions.
Admins can view the status of all auctions at any time.
Auctions are automatically won by the user who places the highest bid when the end time is reached.

This README file provides basic instructions for setting up and running project, 
as well as an overview of user and admin functionalities. 
we can expand it further with more details or custom instructions as needed.
