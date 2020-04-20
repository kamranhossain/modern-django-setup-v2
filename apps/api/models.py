from django.db import models

from django.contrib.auth import get_user_model


class Api(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE
    )
