from django.conf import settings
settings.configure(
    DEBUG=True,
    SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path

posts = [
    {"title": "First Post", "content": "Welcome to my blog"},
    {"title": "Second Post", "content": "Django is powerful"}
]

def home(request):
    html = "<h1>Blog Posts</h1>"

    for i, p in enumerate(posts):
        html += f"""
        <h2>{p['title']}</h2>
        <p>{p['content']}</p>
        <a href="/delete/{i}/">Delete</a>
        <hr>
        """

    return HttpResponse(html)

def delete(request, id):
    if 0 <= id < len(posts):
        posts.pop(id)

    return home(request)

urlpatterns = [
    path("", home),
    path("delete/<int:id>/", delete)
]

from django.core.management import execute_from_command_line
execute_from_command_line(
    ["program.py", "runserver", "0.0.0.0:8004"]
)