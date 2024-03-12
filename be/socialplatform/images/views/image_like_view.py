from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from images.models import Image


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get("id")
    action = request.POST.get("action")
    if not image_id or not action:
        return JsonResponse({"status": "failed"})
    try:
        image = Image.objects.get(id=image_id)
        if action == "like":
            image.users_like.add(request.user)
        else:
            print("GOT HERE")
            image.users_like.remove(request.user)
        return JsonResponse({"status": "success"})
    except Image.DoesNotExist:
        return JsonResponse({"status": "failed"})
