# Hackfest-Tickets-Generator

The Hackfest Ticket Generator is a Django web application that allows users to register for the Hackfest event and generates personalized tickets with QR codes for registered attendees.

## Features

- User Registration:Users can register for the Hackfest event by providing their name, email, team, course, school, programming languages, and year of study.
- QR Code generator: Upon registration, each attendee receives a personalized ticket with a QR code containing their registration information.
- Responsive design: The application is designed to be responsive and work seamlessly on desktop and mobile devices.

## Technologies Used

- Django: Python web framework for building the backend server.
- HTML/CSS/JavaScript: Frontend development for user interface and interactivity.
- Bootstrap: Frontend framework for responsive design and styling.
- qrcode: Python library for generating QR codes.
- SQLite: Lightweight relational database used for storing user registration data.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/H3nryK/Hackfest-Tickets.git

2. Install dependencies:

   ```bash
   pip install django whitenoise pillow qrcode

3. Run migrations to create the database:

   ```bash
   python manage.py migrate

4. Start the development server:

   ```bash
   python manage.py runserver
   
5. Access the application in your web browser at http://localhost:8000/.

## Usage

- Navigate to the home page at the register section.
- Fill out the registration form with your details.
- Submit the form to register for the Hackfest event.
- After successful registration, you will receive a personalized ticket with a QR code.
- Attend the Hackfest event and present your ticket at the registration desk.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.
