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

users = {
    "admin": "1234",
    "user": "5678"
}

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if username in users and users[username] == password:
            return HttpResponse(
                "<h1>Login Successful</h1>"
                "<p>Welcome to Blog Management.</p>"
            )

        return HttpResponse("<h1>Invalid Login</h1>")

    return HttpResponse("""
    <h1>Blog Login</h1>

    <form method="post">
        Username:
        <input name="username"><br><br>

        Password:
        <input type="password" name="password"><br><br>

        <button>Login</button>
    </form>
    """)

urlpatterns = [
    path("", login)
]

from django.core.management import execute_from_command_line
execute_from_command_line(
    ["program.py", "runserver", "0.0.0.0:8009"]
)