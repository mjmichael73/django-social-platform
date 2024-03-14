from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(
        request,
        "account/user/list.html",
        {
            "section": "people",
            "users": users
        }
    )
