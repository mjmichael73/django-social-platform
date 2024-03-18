from images.models import Image
from django.shortcuts import render
import redis
from django.conf import settings
from django.contrib.auth.decorators import login_required

r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


@login_required
def image_ranking(request):
    image_ranking = r.zrange(
        'image_ranking',
        0,
        -1,
        desc=True
    )[:10]
    image_ranking_ids = [int(id) for id in image_ranking]
    most_viewed = list(Image.objects.filter(id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
    return render(
        request,
        'images/image/ranking.html',
        {
            "section": "images",
            "most_viewed": most_viewed
        }
    )
