
# Employee Management API

A Django REST Framework application for managing employees, departments, attendance, performance reviews, JWT authentication, and dashboard reporting.

## Highlights

- Employee and department CRUD APIs
- Attendance and performance modules
- JWT registration, login, and token refresh
- Department employee-count dashboard endpoint
- Swagger and ReDoc API documentation
- Environment-based configuration with a safe local SQLite fallback
- Basic API test coverage for authenticated reporting

## Tech Stack

- Python
- Django 5
- Django REST Framework
- Simple JWT
- django-filter
- drf-yasg
- PostgreSQL or SQLite

## Getting Started

```bash
git clone https://github.com/princechandrasingh/employee_project.git
cd employee_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The app defaults to SQLite for local setup. To use PostgreSQL, set `DATABASE_URL` in `.env`.

## Useful URLs

| URL | Purpose |
| --- | --- |
| `http://127.0.0.1:8000/admin/` | Django admin |
| `http://127.0.0.1:8000/dashboard/` | Department dashboard |
| `http://127.0.0.1:8000/swagger/` | Swagger docs |
| `http://127.0.0.1:8000/redoc/` | ReDoc docs |

## Main API Endpoints

| Endpoint | Description |
| --- | --- |
| `/api/` | API root |
| `/api/register/` | User registration |
| `/api/token/` | Get JWT access and refresh tokens |
| `/api/token/refresh/` | Refresh JWT access token |
| `/api/employees/` | Employee CRUD |
| `/api/departments/` | Department CRUD |
| `/api/attendance/` | Attendance CRUD |
| `/api/performance/` | Performance CRUD |
| `/api/charts/department-employee-count/` | Authenticated dashboard data |

## Example Request

```bash
curl -X GET http://127.0.0.1:8000/api/charts/department-employee-count/ \
  -H "Authorization: Bearer <your-access-token>"
```

## Run Tests

```bash
python manage.py test
```

## Project Structure

```text
employee_project/
|-- attendance/
|-- employees/
|-- performance/
|-- templates/
|-- employee_project/
|-- manage.py
|-- requirements.txt
`-- .env.example
```

## Portfolio Notes

This project demonstrates backend API design, authentication, Django admin usage, relational modeling, API documentation, and environment-based configuration.
