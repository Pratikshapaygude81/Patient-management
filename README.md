# Patient-management
This repository contains the patient management using django rest framework

## Project Overview

A RESTful API developed using Django and Django REST Framework (DRF) for managing patient information and implementing secure user authentication using JWT (JSON Web Tokens).

## Technologies Used

- Python
- Django
- Django REST Framework (DRF)
- Simple JWT
- SQLite

## Features

- Patient Registration
- User Login and Authentication
- JWT Access and Refresh Token Generation
- Access Token Refresh
- Change Password
- Protected API Endpoints
- Secure Password Hashing
- Token-based Authentication

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/patients/register/` | Register a new patient |
| POST | `/api/patients/login/` | Authenticate user and generate JWT tokens |
| POST | `/api/patients/refresh/` | Generate a new access token |
| POST | `/api/patients/change-password/` | Change the authenticated user's password |

## Authentication

The API uses JSON Web Token (JWT) authentication to secure protected endpoints.

- **Access Token:** Used to access protected API resources.
- **Refresh Token:** Used to generate a new access token after expiration.
- **Password Security:** Passwords are securely hashed using Django's built-in password hashing mechanism.

## API Testing

Endpoints can be tested using:

- Postman
- Django REST Framework Browsable API

## Installation and Execution

Install dependencies:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## Project Learning Outcomes

- Django REST API development.
- User authentication and authorization.
- JWT-based authentication.
- Access and refresh token management.
- Secure password management.
- API testing and validation.

## Official Documentation

- Django: https://docs.djangoproject.com/en/6.1/
- Django REST Framework: https://www.django-rest-framework.org/
- Simple JWT: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
