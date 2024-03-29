from django.shortcuts import render
from account.forms import UserRegistrationForm
from account.models import Profile
from actions.helpers import create_action


def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data["password"]
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            return render(
                request,
                "account/register_done.html",
                {
                    "new_user": new_user
                }
            )
    else:
        user_form = UserRegistrationForm()
    return render(
        request,
        "account/register.html",
        {
            "user_form": user_form
        }
    )
