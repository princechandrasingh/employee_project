from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from employees.models import Department, Employee


class DepartmentEmployeeCountTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='recruiter',
            password='strong-test-password',
        )
        self.department = Department.objects.create(name='Engineering')
        Employee.objects.create(
            name='Asha Patel',
            email='asha@example.com',
            phone_number='555-0100',
            address='Austin, TX',
            date_of_joining=date(2025, 6, 3),
            department=self.department,
        )

    def test_department_count_requires_authentication(self):
        response = self.client.get('/api/charts/department-employee-count/')

        self.assertEqual(response.status_code, 403)

    def test_department_count_returns_employee_totals(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/api/charts/department-employee-count/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'name': 'Engineering', 'count': 1}])
