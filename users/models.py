from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    bio = models.TextField(default="Swag")
    image = models.ImageField(default='default.jpg', upload_to='profile-pics')

    def __str__(self):
        return "{} Profile".format(self.user)
