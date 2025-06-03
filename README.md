
# Employee Project

A Django-based Employee Management System for handling employees, departments, attendance, performance, and user authentication with JWT.

### 1. **Clone the Repository**

```bash
cd ~/Documents
git clone https://github.com/princechandrasingh/employee_project.git
cd employee_project
```

### 2. **Set Up a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Apply Migrations**

```bash
python manage.py migrate
```

### 5. **Create a Superuser (for Admin Panel)**

```bash
python manage.py createsuperuser
```

### 6. **Run the Development Server**

```bash
python manage.py runserver
```

### 7. **Access the Application**

- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Dashboard:** [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)
- **API Docs:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## 📚 Features

- Employee & Department CRUD operations
- User Registration with JWT authentication
- Department-wise Employee Bar Chart (dashboard)
- Attendance & Performance modules
- Django Admin Panel for management
- API endpoints for integration
- Swagger & Redoc for API documentation

---

## 🛠️ Main API Endpoints

| Endpoint                                             | Description                          |
|------------------------------------------------------|--------------------------------------|
| `/api/`                                              | API root                             |
| `/api/register/`                                     | User registration (JWT)              |
| `/api/token/`, `/api/token/refresh/`                 | Obtain/refresh JWT tokens            |
| `/api/charts/department-employee-count/`             | Bar graph data (auth required)       |
| `/dashboard/`                                        | Department bar chart dashboard       |

---

## 🔑 Admin Credentials

- Create your own admin credentials using `python manage.py createsuperuser`.

---

## ✨ Example Usage

**Get department employee counts (with JWT):**
```bash
curl -X GET http://127.0.0.1:8000/api/charts/department-employee-count/   -H "Authorization: Bearer <your-access-token>"
```

---

## 📝 Author

- [princechandrasingh](https://github.com/princechandrasingh)

---

## 📝 License

This project is for internal/test/demo use only.
