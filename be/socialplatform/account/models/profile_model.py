from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to="users/%Y/%m/%d/",
        blank=True
    ) # To use ImageField it is necessary to install Pillow

    def __str__(self):
        return f"Profile of {self.user.username}"
