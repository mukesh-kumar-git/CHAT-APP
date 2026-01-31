# Django One-to-One Chat Application

This is a simple one-to-one chat application built using Django, HTML, CSS, and JavaScript.

The project is designed for beginners to understand how real-time–like chat can be implemented using Django without WebSockets or Django Channels.

Messages are sent and received using AJAX (fetch), with data stored in the database.

---

## Features

- User registration and login (Django authentication)
- List of registered users
- One-to-one private chat
- Messages stored in database
- Sender and receiver tracking
- Message timestamp
- WhatsApp-style chat UI (left/right messages)
- No page reload while sending messages
- Beginner-friendly code structure

---

## Tech Stack

Backend:
- Python
- Django

Frontend:
- HTML
- CSS
- JavaScript (Fetch API)

Database:
- SQLite

---

## How the Chat Works

- Users log in using Django authentication
- A logged-in user can see a list of other users
- Selecting a user opens a private chat
- Messages are sent using AJAX (fetch)
- Messages are saved in the database
- Chat messages are fetched periodically without page reload

Note:
This project does NOT use WebSockets or Django Channels.
It focuses on core Django concepts.

---

## Project Structure

chatproject/
|
|-- accounts/          # User authentication
|-- chat/              # Chat logic (models, views, urls)
|-- templates/         # HTML templates
|-- static/            # CSS and JavaScript files
|-- db.sqlite3
|-- manage.py
|-- README.md

---

## Installation and Setup

Step 1: Clone the repository

git clone https://github.com/your-username/django-chat-app.git  
cd django-chat-app

Step 2: Create virtual environment

python -m venv venv

Activate environment (Windows):

venv\\Scripts\\activate

Step 3: Install dependencies

pip install django

Step 4: Apply migrations

python manage.py makemigrations  
python manage.py migrate

Step 5: Create superuser (optional)

python manage.py createsuperuser

Step 6: Run the server

python manage.py runserver

Open browser and go to:

http://127.0.0.1:8000/

---

## Chat Message Details

Each message stores:
- Sender
- Receiver
- Message text
- Timestamp

Messages are displayed:
- On the right for the sender
- On the left for the receiver

---

## Purpose of This Project

- Learn Django fundamentals
- Understand database models and relationships
- Practice AJAX with Django
- Build a real-world beginner chat application
- Prepare for interviews and internships

---

## Limitations

- Not real-time (no WebSockets)
- No group chat
- No media sharing
- No message delivery status

These are intentionally excluded to keep the project simple.

---

## Possible Improvements

- Real-time chat using Django Channels
- Group chat feature
- Message read receipts
- Image and file sharing
- Online/offline user status

---

## Author

Mukesh Kumar TM   
Python | Django | Web Development

---

## Note

This project is built for learning purposes.
The code prioritizes clarity and simplicity over advanced optimizations.
