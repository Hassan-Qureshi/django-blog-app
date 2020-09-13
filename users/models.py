from django.db import models
from django.contrib.auth.models import User
# Reduce Image Size
from PIL import Image

class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    bio = models.TextField(default="Swag")
    image = models.ImageField(default='default.jpg', upload_to='profile-pics')

    """
    Overriding save method. It runs after our model get saved. Overriding just to add some additional functionality
    Functionality Added: It is to reduce the size of image saved
    """
    def save(self):
        super().save()

        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)

    def __str__(self):
        return "{} Profile".format(self.user)
