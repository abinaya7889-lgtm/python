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
    {"name": "Anu", "age": 20, "course": "BCA"},
    {"name": "Ravi", "age": 21, "course": "B.Com"}
]

def home(request):
    html = "<h1>Student Records</h1>"

    for i, student in enumerate(students):
        html += f"""
        <p>
        {student['name']} - {student['age']} - {student['course']}
        <a href="/edit/{i}/">Edit</a>
        </p>
        """

    return HttpResponse(html)

def edit_student(request, id):
    student = students[id]

    if request.method == "POST":
        student["name"] = request.POST.get("name")
        student["age"] = request.POST.get("age")
        student["course"] = request.POST.get("course")
        return home(request)

    return HttpResponse(f"""
    <h1>Edit Student</h1>

    <form method="post">
        Name:
        <input type="text" name="name" value="{student['name']}"><br><br>

        Age:
        <input type="number" name="age" value="{student['age']}"><br><br>

        Course:
        <input type="text" name="course" value="{student['course']}"><br><br>

        <button type="submit">Update</button>
    </form>
    """)

urlpatterns = [
    path('', home),
    path('edit/<int:id>/', edit_student),
]

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program4.py",
        "runserver",
        "0.0.0.0:8005"
    ])