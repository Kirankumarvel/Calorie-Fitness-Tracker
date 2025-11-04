# 🏋️ FitTrack a.k.a Calorie/Fitness Tracker

A comprehensive web application built with Django to track daily calorie intake and exercise expenditure. Monitor your fitness journey with intuitive data visualization and personalized insights.

![Django](https://img.shields.io/badge/Django-4.2.7-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

### 🔐 User Authentication
- User registration & login (secure)
- Personalized dashboard (user-specific data)
- Session management and persistence

### 📊 Calorie Tracking
- Food intake logging (meals and calories)
- Exercise logging (workouts and calories burned)
- Daily summaries: food, exercise, and net calories
- Historical entries: view and manage past logs

### 📈 Data Visualization
- Weekly interactive charts (7-day trends)
- Multiple metrics: food, exercise, net calories
- Visual insights for easy understanding

### 🛠 Management Features
- Full CRUD for entries
- Django admin for administration
- Form validation for data integrity

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd Calorie_trackerapp
   ```

2. Create and activate a virtual environment

   Windows
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   macOS / Linux
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. (Optional) Create a superuser
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server
   ```bash
   python manage.py runserver
   ```

7. Open the app
   - Go to http://127.0.0.1:8000 in your browser

---

## 📁 Project Structure

Calorie_trackerapp/
├── calorie_tracker/          # Django project settings  
│   ├── settings.py           # Project configuration  
│   ├── urls.py               # Main URL routing  
│   └── wsgi.py               # WSGI configuration  
├── tracker/                  # Main application  
│   ├── models.py             # Database models  
│   ├── views.py              # Business logic and views  
│   ├── urls.py               # App-specific URLs  
│   ├── forms.py              # Form definitions  
│   ├── admin.py              # Admin interface configuration  
│   └── templates/            # HTML templates  
│       └── tracker/  
│           ├── base.html  
│           ├── dashboard.html  
│           ├── charts.html  
│           └── ...  
├── static/                   # Static files (CSS, images)  
├── manage.py                 # Django management script  
└── requirements.txt          # Project dependencies

---

## 🎯 Usage Guide

### For End Users
- Registration & Login: Create an account or sign in.
- Add Entry: Click "Add Entry", choose type (Food/Exercise), provide name, calories, and date.
- Dashboard: See today's totals and recent entries.
- Charts: View 7-day trends and insights.
- Manage Entries: Edit or delete entries via "My Entries".

### For Administrators
- Admin Access: Visit `/admin` and log in with superuser credentials.
- Manage users, entries and other site data via the Django admin.

---

## 🛠 Tech Stack

Backend
- Django 4.2.7
- Python 3.8+

Database
- SQLite (development)
- Django ORM

Frontend
- Django templates (server-side rendering)
- HTML5 / CSS3
- Matplotlib for charts

Security
- Django Auth (authentication & sessions)
- CSRF protection
- Server-side form validation

---

## 🔧 API Endpoints (Overview)

Method | URL | Description
---|---:|---
GET | / | Home page
GET/POST | /register/ | User registration
GET/POST | /login/ | User login
POST | /logout/ | User logout
GET | /dashboard/ | User dashboard
GET/POST | /tracker/add/ | Add new calorie entry
GET | /tracker/entries/ | List user entries
POST | /tracker/delete/<id>/ | Delete entry
GET | /tracker/charts/ | Weekly charts

---

## 🐛 Troubleshooting

Common issues and fixes:

- ModuleNotFoundError: No module named 'django'
  ```bash
  pip install django
  ```

- NumPy compatibility issues
  ```bash
  pip install "numpy<2" matplotlib==3.7.2
  ```

- Static files warning
  ```bash
  mkdir -p static static/css static/images
  ```

- Migrations not detected
  ```bash
  python manage.py makemigrations tracker
  ```

Note: The app runs in DEBUG mode by default. Set DEBUG = False in production.

---

## 🚀 Deployment (Production Guidance)

- Set DEBUG = False and configure ALLOWED_HOSTS
- Use a production DB (PostgreSQL recommended)
- Serve with Gunicorn (or another WSGI server)
- Configure static file serving (WhiteNoise, CDN, or web server)
- Use environment variables for secrets
- Consider hosting on Heroku, PythonAnywhere, AWS, or DigitalOcean

---

## 🤝 Contributing

We welcome contributions!

Steps:
1. Fork the repo
2. Create a feature branch
3. Make changes and add tests if applicable
4. Submit a pull request

---

## 📄 License

MIT License — see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Django Software Foundation
- Matplotlib Team
- Python community

---

## 📞 Support

If you run into issues:
- Check the Troubleshooting section
- Search existing GitHub issues
- Open a new issue with a detailed description

Built with ❤️ using Django and Python
