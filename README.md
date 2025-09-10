

# 📚 Learning Platform API

A **Django REST Framework** project that provides APIs for managing a Learning Platform (mini LMS).
It supports authentication via **JWT**, role-based permissions, course management, enrollments, progress tracking, and reviews.

---

## 🚀 Features

* 👨‍🎓 **Students & Teachers** management
* 📚 **Courses & Subjects** with teacher assignments (by admin)
* 📝 **Course Info** (description, duration, etc.)
* 🎓 **Enrollments** – students can enroll in courses
* 📊 **Progress tracking** for students
* ⭐ **Course Reviews** (per course)
* 🌍 **Platform Reviews** (for overall platform)
* 🔑 **JWT Authentication** (login, refresh tokens)
* 🔒 **Permissions** – Admin manages teachers/courses, students only enroll/review
* 🔍 **Search & Filtering** for courses/teachers

---

## ⚙️ Tech Stack

* **Python 3.11+**
* **Django 5.x**
* **Django REST Framework**
* **JWT (djangorestframework-simplejwt)**
* **django-filter** for filtering
* **MySQL / SQLite** (configurable)

---

## 🛠️ Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/learning-platform.git
cd learning-platform
```

### 2. Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run migrations & create superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run server

```bash
python manage.py runserver
```

Now visit: 👉 `http://127.0.0.1:8000/api/`

---

## 🔑 Authentication (JWT)

### Obtain Token

`POST /api/token/`

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Response:

```json
{
  "refresh": "refresh_token_here",
  "access": "access_token_here"
}
```

### Refresh Token

`POST /api/token/refresh/`

```json
{
  "refresh": "refresh_token_here"
}
```

---

 📘 API Documentation

 👨‍🎓 Students

* `GET /api/students/` → List students
* `POST /api/students/` → Create student

### 👨‍🏫 Teachers

* `GET /api/teachers/` → List teachers
* `POST /api/teachers/` *(Admin only)* → Add teacher

### 📚 Courses

* `GET /api/courses/` → List courses
* `POST /api/courses/` *(Admin only)* → Create course with assigned teachers

### 📝 Course Info (per course)

* `GET /api/courses/{course_id}/courseinfo/`
* `POST /api/courses/{course_id}/courseinfo/` *(Admin only)*

### 📖 Subjects (per course)

* `GET /api/courses/{course_id}/subjects/`
* `POST /api/courses/{course_id}/subjects/` *(Admin only)*

### 🎓 Enrollment

* `GET /api/enrollments/` → List enrollments
* `POST /api/enrollments/` → Enroll a student into a course

### 📊 Progress

* `GET /api/progress/` → List progress
* `POST /api/progress/` → Add/update student progress

 ⭐ Course Reviews (per course)

* `GET /api/courses/{course_id}/reviews/`
* `POST /api/courses/{course_id}/reviews/` *(Student only)*

### 🌍 Platform Reviews

* `GET /api/platformreviews/`
* `POST /api/platformreviews/`

---

## 🔒 Permissions

* **Admin** → Manage teachers, courses, subjects, course info.
* **Students** → Enroll in courses, track progress, write reviews.
* **Anyone** → Can view public data (courses, teachers, reviews).

---

## 📌 Example API Request

Enroll student in a course:

```json
POST /api/enrollments/
{
  "student": 1,
  "course": 2
}
```

Response:

```json
{
  "id": 10,
  "student": 1,
  "course": 2,
  "status": "enrolled"
}
```

---


