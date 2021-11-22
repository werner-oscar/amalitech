from django.db import models
from django.contrib.auth.models import User


class UserImages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=500)
