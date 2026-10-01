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
    {"title": "Python Programming", "content": "Learn Python"},
    {"title": "Django Framework", "content": "Build web applications"},
    {"title": "HTML Tutorial", "content": "Learn web design"}
]

def home(request):
    return HttpResponse("""
    <h1>Blog Search</h1>

    <form action="/search/">
        <input name="q" placeholder="Search posts">
        <button>Search</button>
    </form>
    """)

def search(request):
    q = request.GET.get("q", "").lower()

    html = f"<h1>Search Results for: {q}</h1>"

    for p in posts:
        if q in p["title"].lower() or q in p["content"].lower():
            html += f"""
            <h2>{p['title']}</h2>
            <p>{p['content']}</p>
            <hr>
            """

    return HttpResponse(html)

urlpatterns = [
    path("", home),
    path("search/", search)
]

from django.core.management import execute_from_command_line
execute_from_command_line(
    ["program.py", "runserver", "0.0.0.0:8007"]
)