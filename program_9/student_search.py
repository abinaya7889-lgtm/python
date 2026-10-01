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
    {"name": "Karthik", "age": 22, "course": "B.Com"}
]

def home(request):
    html = """
    <h1>Student Search</h1>

    <form method="get" action="/search/">
        Enter Name:
        <input type="text" name="name">
        <button>Search</button>
    </form>

    <h2>All Students</h2>
    """

    for student in students:
        html += f"""
        <p>
        {student['name']} -
        {student['age']} -
        {student['course']}
        </p>
        """

    return HttpResponse(html)

def search(request):
    name = request.GET.get("name", "").lower()

    html = "<h1>Search Result</h1>"

    for student in students:
        if name in student["name"].lower():
            html += f"""
            <p>
            Name: {student['name']}<br>
            Age: {student['age']}<br>
            Course: {student['course']}
            </p>
            """

    html += '<a href="/">Back</a>'

    return HttpResponse(html)

urlpatterns = [
    path('', home),
    path('search/', search),
]

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program5.py",
        "runserver",
        "0.0.0.0:8003"
    ])