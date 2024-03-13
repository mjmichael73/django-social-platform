from lib2to3.btm_utils import syms

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class Contact(models.Model):
    user_from = models.ForeignKey(
        'auth.User',
        related_name="rel_from_set",
        on_delete=models.CASCADE
    )
    user_to = models.ForeignKey(
        'auth.User',
        related_name="rel_to_set",
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"


user_model = get_user_model()
user_model.add_to_class(
    'following',
    models.ManyToManyField(
        'self',
        through=Contact,
        related_name='followers',
        symmetrical=False
    )
)
