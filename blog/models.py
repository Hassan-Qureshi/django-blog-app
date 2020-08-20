from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now=True) # Always update the date even if it's updated that's not required
    # date_posted = models.DateTimeField(auto_now_add=True)
