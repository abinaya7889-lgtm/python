import os
import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='student123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
    INSTALLED_APPS=['django.contrib.contenttypes'],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'students.db',
        }
    }
)

django.setup()

from django.http import HttpResponse
from django.urls import path

students = [
    {"name": "Arun", "age": 20, "course": "BCA"},
    {"name": "Priya", "age": 21, "course": "B.Sc"},
    {"name": "Kumar", "age": 20, "course": "B.Com"}
]

def home(request):
    html = "<h1>Student List</h1>"

    for i, student in enumerate(students):
        html += f"""
        <p>
        {student['name']} -
        {student['course']}
        <a href="/detail/{i}/">View Details</a>
        </p>
        """

    return HttpResponse(html)

def detail(request, id):
    student = students[id]

    return HttpResponse(f"""
    <h1>Student Details</h1>
    <p>Name: {student['name']}</p>
    <p>Age: {student['age']}</p>
    <p>Course: {student['course']}</p>
    <a href="/">Back</a>
    """)

urlpatterns = [
    path('', home),
    path('detail/<int:id>/', detail),
]

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program2.py",
        "runserver",
        "0.0.0.0:8002"
    ])