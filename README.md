# 🎓 StudentZone – Django Student Management System

**StudentZone** is a full-stack Django web app for managing student-related operations in colleges or universities. It supports student admissions, login/logout, enquiries, marksheets, and more.

---

## 🚀 Features

- 🔐 User Signup, Login & Logout
- 📝 Enquiry Form for Prospective Students
- 🧾 Admission Form for PG & PhD Courses
- 📄 Marksheet Entry & Search
- 🔍 Marksheet Search by Enrollment Number
- 🖼️ Student Photo Upload (with Pillow)
- ⏱️ Session Timeout after 5 Minutes of Inactivity

---

## 🛠 Tech Stack

- **Backend:** Django 5.1, Python 3
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** MySQL (can switch to SQLite)
- **Media Handling:** Pillow for image uploads

---

## 📸 Screenshots


- ![Login Page]("screenshort\loginpage.png")
- ![Admission Form]("screenshort\admission form.png")
- ![Marksheet View]("screenshort\markshhet.png")

---

## ⚙️ Setup Instructions

### 🧑‍💻 Clone the Project

```bash
git clone https://github.com/Rahul-kumar-70/student_zone.git
cd studentzone

### Create a Virtual Environment
 python -m venv env
env\Scripts\activate

### Install Required Packages
 pip install -r requirements.txt
 pip freeze > requirements.txt

###Configure Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'collegestudent',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

### Run Migrations
python manage.py makemigrations
python manage.py migrate

### Create Superuser (Admin Login)
python manage.py createsuperuser

###Run the Server
python manage.py runserver

###Then open your browser and visit:
http://127.0.0.1:8000/

###Test Credentials (if you have demo users)
Username: RahulKumar
Password: Rahul@123
