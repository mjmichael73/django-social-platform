from django.shortcuts import render, get_object_or_404
from images.models import Image
import redis
from django.conf import settings

r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
)


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    total_views = r.incr(f'image:{image.id}:views')
    r.zincrby('image_ranking', 1, image.id)
    return render(
        request,
        "images/image/detail.html",
        {
            "section": "images",
            "image": image,
            "total_views": total_views
        }
    )
