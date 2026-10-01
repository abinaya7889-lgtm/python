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
    {
        "title": "Django Blog",
        "content": "This is a Django post.",
        "comments": []
    }
]

def home(request):
    html = "<h1>Blog with Comments</h1>"

    for i, p in enumerate(posts):
        html += f"""
        <h2>{p['title']}</h2>
        <p>{p['content']}</p>

        <h3>Comments</h3>
        """

        for c in p["comments"]:
            html += f"<p>💬 {c}</p>"

        html += f"""
        <form method="post" action="/comment/{i}/">
            <input name="comment"
                   placeholder="Write a comment">
            <button>Add Comment</button>
        </form>
        <hr>
        """

    return HttpResponse(html)

def comment(request, id):
    if request.method == "POST":
        posts[id]["comments"].append(
            request.POST["comment"]
        )

    return home(request)

urlpatterns = [
    path("", home),
    path("comment/<int:id>/", comment)
]

from django.core.management import execute_from_command_line
execute_from_command_line(
    ["program.py", "runserver", "0.0.0.0:8005"]
)