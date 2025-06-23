from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


def login_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "users/register_success.html", {"user": user})
        else:
            return render(
                request, "users/register.html", {"error": "Invalid credentials"}
            )

    return render(request, "users/register.html")
