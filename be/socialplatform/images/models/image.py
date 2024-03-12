from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    image_file = models.ImageField(upload_to="images/%Y/%m/%d/")
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)

    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="images_liked",
        blank=True
    )

    class Meta:
        indexes = [
            models.Index(fields=['created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        base_url = "http://127.0.0.1:8000/media/"
        return base_url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
