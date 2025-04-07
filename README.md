# 📝 Todo API

A simple Todo API built with Django REST Framework.  
It supports JWT-based authentication and basic features like filtering, searching, and marking tasks as done, full API documentation via Swagger and Redoc.

---

## 🚀 Features

- JWT authentication (Login & Register)
- Create / update / delete personal tasks
- Task categories per user
- Filtering, searching, and ordering tasks
- Mark tasks as done
- API documentation with Swagger and Redoc

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT (authentication)
- Django Filter
- drf-yasg (Swagger / Redoc)

---

## 📦 Installation

```bash
git clone https://github.com/amirpashayi-dev/todo-api.git
cd todo-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📚 API Documentation

- Swagger: http://127.0.0.1:8000/swagger/
- Redoc: http://127.0.0.1:8000/redoc/

---

## 🔐 Authentication (JWT)

### Register
`POST /api/accounts/register/`

### Login
`POST /api/accounts/token/`

Example request body:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Use the returned access token like:
```
Authorization: Bearer <access_token>
```

---

## ✅ Mark Task as Done

`PATCH /api/tasks/<id>/done/`  
This endpoint sets the `is_done` field of a task to `true`.

---

## 📁 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | /api/accounts/register/        | Register new user |
| POST   | /api/accounts/token/           | Login & get tokens |
| GET/POST | /api/tasks/                  | List / create tasks |
| GET/PUT | /api/tasks/{id}/              | Retrieve / update task |
| PATCH   | /api/tasks/{id}/done/         | Mark task as done |
| GET/POST | /api/categories/             | List / create categories |
| GET/PUT/DELETE | /api/categories/{id}/  | Retrieve / update / delete category |

---

## 👨‍💻 Developer Notes

This project is built as a personal portfolio API to demonstrate real-world backend skills.  
It follows best practices in:

- Authentication & Permissions
- Filtering & Searching
- Clean code structure
- API documentation

---

## 👤 Author

Created by **Amir Pashayi**  
[GitHub: amirpashayi-dev](https://github.com/amirpashayi-dev)
