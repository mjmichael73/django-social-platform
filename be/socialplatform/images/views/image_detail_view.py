from django.shortcuts import render, get_object_or_404
from images.models import Image


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(
        request,
        "images/image/detail.html",
        {
            "section": "images",
            "image": image
        }
    )
