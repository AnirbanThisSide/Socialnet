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

## 📁 Project Structure
Socialnet-Django/
├── core/ # Core Django app with models, views, urls
├── templates/ # HTML templates for rendering pages
├── static/ # Static files (CSS/JS)
├── db.sqlite3 # Default SQLite database
├── manage.py # Django management script
└── requirements.txt # (optional) Python package list

---

## ⚙️ Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AnirbanThisSide/Socialnet.git
   cd Socialnet
   
(Optional) Create virtual environment:  
python -m venv venv
venv\Scripts\activate  # Windows

Install dependencies:
pip install django

Run the development server:
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to use the app.
