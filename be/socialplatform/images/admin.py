from django.contrib import admin
from images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "image_file", "created"]
    list_filter = ["created"]
