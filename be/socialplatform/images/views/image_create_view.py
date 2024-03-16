from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from images.forms import ImageCreateForm
from actions.helpers import create_action


@login_required
def image_create(request):
    if request.method == "POST":
        form = ImageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            create_action(request.user, 'bookmarked image', new_image)
            messages.success(request, "Image added successfully.")
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm()
    return render(
        request,
        "images/image/create.html",
        {
            "section": "images",
            "form": form
        }
    )
