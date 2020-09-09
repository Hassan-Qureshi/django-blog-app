from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
Following is the receiver which triggers when it receive post_save signal and the sender is `User`
If we don't specify sender the method will be fired after each save in database
The decorator runs first and makes sure that the signal and sender are correct.
"""


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.profile.save()
