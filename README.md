# admission_counselling
📘 Admission Counselling System

A full-stack Django-based Admission Counselling Web Application designed to help students explore courses, watch educational content, read testimonials, and connect for guidance.

🚀 Features
🎓 Course listing and details
📺 YouTube video integration (educational content)
🧑‍🎓 Student testimonials section
📩 Contact/Enquiry system
🔍 Search and category filtering (if enabled)
📱 Responsive UI (mobile + desktop friendly)
⚙️ Admin panel for managing content
🛠️ Tech Stack
    Backend: Django (Python)
    Frontend: HTML, CSS, JavaScript
    Database: SQLite3 (default Django DB)
    Styling: Custom CSS
    Other: Django Admin Panel

    
📁 Project Structure
admission_counselling/
│
├── counselling/        # Main project settings
├── courses/            # Course module
├── yt/                 # YouTube integration
├── ytdata/             # Video data handling
├── testimonials/       # Student reviews
├── contactus/          # Contact form
├── aboutus/            # About page
├── banner/             # UI banners
├── common/             # Shared components
├── db.sqlite3          # Database (not recommended for production)
├── manage.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/navika2025/admission_counselling.git
cd admission_counselling

3. Create virtual environment
python -m venv .venv

Activate:
Windows
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

5. Run migrations
python manage.py migrate

7. Create superuser (optional)
python manage.py createsuperuser

9. Run server
python manage.py runserver

🌐 Open in browser
http://127.0.0.1:8000/



Author
navika2025
GitHub: https://github.com/navika2025
