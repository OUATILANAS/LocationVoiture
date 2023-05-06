# Car Rental Web Application

This is a car rental web application built with Django, allowing users to rent cars and manage their rental orders.

## Technologies Used

- Python3
- Django
- HTML
- CSS
- JavaScript
- Bootstrap
- BeautifulSoup

## Features

- View a list of available cars
- Check car details
- Book a car for a specific date and time
- Admin panel to manage cars and bookings and add users

## Getting Started

1. Clone the repository to your local machine:

git clone https://github.com/OUATILANAS/LocationVoiture.git

2. Change to the project directory:

cd LocationVoiture

3. Create a new database and configure the database settings in the settings.py file.

Database Name : Django

4. Run the migrations using the following command:

python3 manage.py migrate

5. Create a superuser account to access the admin panel:

python3 manage.py createsuperuser

6. Start the development server using the following command:

python3 manage.py runserver

7. Open your web browser and navigate to http://localhost:8000 to view the application.

## Usage

### Navigation

The application has the following pages:

- Home page: displays a list of available cars and allows users to search for specific cars by make, model, or year.
- Car details page: displays detailed information about a specific car, including its make, model, year, and rental price.
- Rental page: allows users to rent a car by selecting the rental period and entering their contact information.
- Login page: allows users to log in to their account.
- Signup page: allows users to create a new account.
- Profile page: allows users to view and manage their rental orders.
- Logout: logs the user out of their account.

### Adding and Managing Cars

- To add a new car to the inventory, go to the admin panel 
by going to http://localhost:8000/login/ and log in with your superuser account.
- Click on "Cars" under the "Car Rental" section.
- Click on "Add Car" and enter the details of the new car, including its make, model, year, rental price, and an image of the car.
- To edit or delete an existing car, go to the car details page and click on "Edit" or "Delete".

## URLs

The application has the following URLs:

- /user: displays the profile page of the currently logged-in user.
- /adduser: allows a user to create a new account.
- /about: displays information about the application.
- /blog-single: displays a single blog post.
- /blog: displays a list of blog posts.
- /car-single/int:id: displays detailed information about a specific car.
- /car: displays a list of available cars.
- /contact: displays a contact form.
- /services: displays a list of services offered.
- /home: displays the home page.
- /addnew: allows a superuser to add a new car to the inventory.
- /edit/id: allows a superuser to edit the details of an existing car.
- /update/id: updates the details of an existing car.
- /delete/id: deletes an existing car.
- /login: displays the login form.
- /signup: displays the signup form.
- /logout: logs the user out of their account.
- /rent-a-car: allows users to rent a car.
- /scraptitle : allows user to get a header from a website using BeautifulSoup

## Credits
This application was built by Ouatil Anas,Nabil Sas and Aya Kharbouch using Django and Bootstrap.






