from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from account.forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponse("Invalid input data.")
        cd = form.cleaned_data
        user = authenticate(
            request,
            username=cd["username"],
            password=cd["password"]
        )
        if not user:
            return HttpResponse("Invalid credentials.")
        if not user.is_active:
            return HttpResponse("Disabled account.")
        login(request, user)
        return HttpResponse("Authenticated successfully.")
    else:
        form = LoginForm()
    return render(
        request,
        "account/login.html",
        {
            "form": form
        }
    )
