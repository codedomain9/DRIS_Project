# DRIS-NADMA Project 🛟

This Django-based Disaster Response Information System (DRIS) is designed to support citizen aid requests, volunteer task coordination, and admin disaster management under a unified web portal.

---

## ⚙️ Setup Instructions

```bash
python -m venv venv
# Activate virtual environment
venv\Scripts\activate         # For Windows
source venv/bin/activate      # For macOS/Linux

pip install django
python manage.py runserver


🌐 DRIS-NADMA Website (Citizen)
-User Signup: http://127.0.0.1:8000/signup/
-User Login: http://127.0.0.1:8000/accounts/login/
-Dashboard / Home (Login Required): http://127.0.0.1:8000/
-Disaster Report: http://127.0.0.1:8000/disasters/
-Submit Aid Request: http://127.0.0.1:8000/aid-request/
-My Submissions (Aid Requests): http://127.0.0.1:8000/my-submissions/
-Shelter Directory: http://127.0.0.1:8000/citizen/shelters/

🧑‍🤝‍🧑 DRIS-NADMA Volunteer Portal
-Volunteer Signup: http://127.0.0.1:8000/volunteer/signup/
-Volunteer Login: http://127.0.0.1:8000/volunteer/login/
-Volunteer Home: http://127.0.0.1:8000/volunteer/
-Register Skills & Availability: http://127.0.0.1:8000/volunteer/register/
-Assigned Tasks: http://127.0.0.1:8000/volunteer/tasks/
-Shelter Directory: http://127.0.0.1:8000/volunteer/shelters/

🔐 DRIS-NADMA Admin Management
-Admin Login: http://127.0.0.1:8000/admin/login/?next=/admin/
-Admin Dashboard: http://127.0.0.1:8000/admin/

✏️ Admin Controls
-Aid Requests: http://127.0.0.1:8000/admin/dris_app/aidrequest/
-Disaster Reports: http://127.0.0.1:8000/admin/dris_app/disasterreport/
-Shelters: http://127.0.0.1:8000/admin/dris_app/shelter/
-Users: http://127.0.0.1:8000/admin/dris_app/user/
-Volunteer Assignments: http://127.0.0.1:8000/admin/volunteer/volunteerassignment/
-Volunteer Skills: http://127.0.0.1:8000/admin/volunteer/volunteerskill/

🧾 Demo Credentials
Username: 23100598
Password: admin123

## Developer
Master in Software Engineering – Universiti Malaya
Name: Lee Kei Kar  
Student ID: 23100598
