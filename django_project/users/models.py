# Useful links:
# https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # One to one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_imgs')

    def __str__(self):
        return f"{self.user.username} Profile"
