from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from actions.models import Action


@login_required
def dashboard(request):
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related("user", "user__profile").prefetch_related("target")[:10]
    return render(
        request,
        "account/dashboard.html",
        {
            "section": "dashboard",
            "actions": actions
        }
    )
