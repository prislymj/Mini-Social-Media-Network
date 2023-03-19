For this mini social network project, I chose to use HTML and CSS for designing and styling the user interface of the application. As for the database, I chose MySQL as I have prior knowledge and it is a popular relational database management system that can store user data such as login credentials, user profiles, and friends list.

I also chose to use Python web framework Flask as it is easy to learn and use. Here, it is used for creation of dynamic web pages and database connectivity. Flask provides easy-to-use and flexible routing system that enables users to interact with the database through a variety of HTTP requests.

To interact with MySQL, I used SQLAlchemy, an open-source SQL toolkit and ORM (Object-Relational Mapping) for Python. It allows the application to easily map database tables to classes, and interact with the database using Python methods instead of writing raw SQL statements.

In this project, I created a Flask web application that allows users to sign up, log in, create profiles, and search for other users. The User and UserProfile classes define the database schema for the users and their profiles. The User class stores the basic information of a user (name, email, and password), while the UserProfile class stores additional information such as the user's date of birth, phone number, bio, and image URL.

* Templates folder contains front-end(all HTML pages). Static folder contains CSS styling
* app.py is the main Python file that contains the Flask application. This file is responsible for handling incoming HTTP requests, rendering HTML templates, and returning appropriate responses to the client.
    * Importing the required modules and dependencies, such as Flask, SQLAlchemy, etc.
    * Defining various routes (URLs) and their corresponding functions to handle HTTP requests.
    * Defining database models using SQLAlchemy to represent the database tables and their relationships.


The application includes several routes, including:

* The home route ('/') returns the index.html template.
* The add_user route ('/add_user') allows users to sign up by providing their name, email, and password. This route adds a new user to the database.
* The login route ('/login') allows users to log in by providing their email and password. This route checks the provided email and password against the database and sets a user session if the credentials are valid.
* The profile route ('/profile') allows users to view their own profile after logging in. This route retrieves the user ID from the session and uses it to query the User model to retrieve the user's name.
* The create_profile route ('/create_profile') allows users to create their own profiles by providing additional information such as their date of birth, phone number, bio, and image URL. This route adds a new UserProfile object to the database.
* The edit_profile route ('/profile/edit') allows users to edit their own profile information. This route uses the EditProfileForm class to validate and populate a form with the user's information, allowing them to edit and submit the updated information to the database.
* The search route ('/search') allows users to search for other users by name. If a query string is provided, this route uses SQLAlchemy to search the User model for all users whose name matches the query. If no query string is provided, this route returns all users in the database.

Additionally, I implemented a login_required decorator that restricts access to certain routes (such as the profile and edit_profile routes) to logged-in users only.


Running the code:

To run the code, follow these steps:

Install Flask and SQLAlchemy using pip:
pip install Flask
pip install SQLAlchemy
Clone or download the project from the GitHub repository.

Create a MySQL database by running the following command in your MySQL terminal:
CREATE DATABASE mini_social_network;
Edit the config.py file in the project directory to set your MySQL database credentials.

Run the app.py file to start the Flask application:
python app.py
Open your web browser and go to http://localhost:5000 to access the home page of the mini social network.

You can now sign up, log in, create a profile, and search for other users
