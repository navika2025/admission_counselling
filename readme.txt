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
├── counselling/ # Core project settings
├── courses/ # Course management module
├── yt/ # YouTube integration module
├── ytdata/ # Video data handling
├── testimonials/ # Student feedback system
├── contactus/ # Contact & enquiry system
├── aboutus/ # About page
├── banner/ # UI banners & homepage visuals
├── common/ # Shared utilities/components
│
├── db.sqlite3 # Development database
├── manage.py # Django entry point
├── requirements.txt # Dependencies
└── README.md


---

## ⚙️ Getting Started

1️⃣ Clone the Repository
```bash
git clone https://github.com/navika2025/admission_counselling.git
cd admission_counselling

2️⃣ Create Virtual Environment
python -m venv .venv

Activate it:
Windows
.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate

5️⃣ Create Admin User
python manage.py createsuperuser

6️⃣ Run Development Server
python manage.py runserver


🌐 Access Application
Local URL: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/


📈 Future Enhancements
🔐 User authentication system (students login)
☁️ Cloud deployment (AWS / Render / Railway)
🗄️ PostgreSQL integration for production
📱 Mobile-first UI improvements
⚡ REST API integration (Django REST Framework)
👨‍💻 Developer

navika2025

GitHub: https://github.com/navika2025
Project: Admission Counselling Platform
⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub — it helps a lot!
