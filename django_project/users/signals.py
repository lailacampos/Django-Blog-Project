# Useful links:
# https://docs.djangoproject.com/en/4.0/topics/signals/
# https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8
# https://realpython.com/primer-on-python-decorators/
# https://docs.djangoproject.com/en/4.0/topics/signals/#connecting-to-signals-sent-by-specific-senders

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# User profile created for each new user


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
