from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Department, Employee
from attendance.models import Attendance
from performance.models import Performance
from datetime import timedelta, datetime

class Command(BaseCommand):
    help = "Seed database with fake employees, departments, attendance, and performance data."

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data
        Attendance.objects.all().delete()
        Performance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()

        # Create Departments
        department_names = ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'Operations']
        departments = [Department.objects.create(name=name) for name in department_names]

        # Initialize employees list
        employees = []

        # Create Employees
        for _ in range(50):
            phone = fake.phone_number()[:50]
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=phone,
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(departments),
            )
            employees.append(emp)

        # Create Attendance for last 30 days
        status_choices = ['Present', 'Absent', 'Late']
        today = datetime.today().date()
        for emp in employees:
            for day_delta in range(30):
                date = today - timedelta(days=day_delta)
                Attendance.objects.create(
                    employee=emp,
                    date=date,
                    status=random.choices(status_choices, weights=[0.8, 0.15, 0.05])[0]
                )

        # Create Performance records (3 reviews per employee)
        for emp in employees:
            for _ in range(3):
                review_date = fake.date_between(start_date=emp.date_of_joining, end_date='today')
                rating = random.randint(1, 5)
                Performance.objects.create(
                    employee=emp,
                    rating=rating,
                    review_date=review_date,
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
