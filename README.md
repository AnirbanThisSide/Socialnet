# 🌐 SocialNet

A Django-based social networking platform that allows users to register, log in, and share posts in a minimalistic social feed. Built from the ground up with a focus on clean architecture and simplicity.

---

## 🚀 Features

- User authentication (Signup, Login, Logout)
- Create, view, and delete posts
- Responsive user feed
- Clean and organized Django app structure

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML (with Django Templates)
- **Database:** SQLite (default with Django)

---

Socialnet-Django/
├── core/              # Core Django app with models, views, urls
├── templates/         # HTML templates for rendering pages
├── static/            # Static files (CSS/JS)
├── db.sqlite3         # Default SQLite database
├── manage.py          # Django management script
└── requirements.txt   # (optional) Python package list


---

## ⚙️ Getting Started

This guide will help you set up and run the SocialNet project locally on your machine.

---

## 📥 Step 1: Clone the Repository

Open your terminal or PowerShell and run:

```bash
git clone https://github.com/AnirbanThisSide/Socialnet.git
cd Socialnet
python -m venv venv

venv\Scripts\activate  # For Windows users
source venv/bin/activate  # For macOS/Linux users

pip install django

python manage.py runserver

http://127.0.0.1:8000/
```
---------------------------------
# ⚙️ Useful Django Commands

```
python manage.py migrate  # Run migrations

python manage.py createsuperuser # Create a superuser (admin access)
python manage.py collectstatic # Collect static files (for production)
