# 🚀 Admission Counselling Platform

> A modern full-stack **Django-based Admission Counselling Platform** designed to help students explore courses, access educational videos, read testimonials, and connect for academic guidance.

---

## ✨ Overview

The **Admission Counselling Platform** is built to simplify the student decision-making process by providing structured course information, curated educational content, and direct enquiry options — all in one place.

This project demonstrates real-world full-stack development using Django with a focus on scalability, modular design, and clean UI.

---

## 🎯 Key Features

### 🎓 Smart Course Management
- Browse available courses
- Organized course structure
- Easy navigation for students

### 📺 Educational Video Integration
- YouTube-based learning content
- Categorized video library
- Embedded playback experience

### 🧑‍🎓 Testimonials System
- Student feedback showcase
- Real experience highlights
- Trust-building UI section

### 📩 Enquiry & Contact System
- Direct student inquiries
- Simple communication workflow
- Admin-managed responses

### ⚙️ Admin Dashboard
- Full content control via Django admin
- Manage courses, videos, testimonials

---

## 🧱 Tech Stack

| Layer        | Technology |
|--------------|------------|
| Backend      | Django (Python) |
| Frontend     | HTML, CSS, JavaScript |
| Database     | SQLite3 (development) |
| UI Styling   | Custom CSS |
| Architecture | Modular Django Apps |

---

## 📁 Project Architecture

admission_counselling/
│
├── counselling/
├── courses/
├── yt/
├── ytdata/
├── testimonials/
├── contactus/
├── aboutus/
├── banner/
├── common/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/navika2025/admission_counselling.git
cd admission_counselling

2. Create virtual environment
python -m venv .venv

Activate on Windows:
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Create superuser (optional)
python manage.py createsuperuser

6. Run server
python manage.py runserver


🌐 Open in browser
http://127.0.0.1:8000/


👨‍💻 Author
navika2025
GitHub: https://github.com/navika2025


