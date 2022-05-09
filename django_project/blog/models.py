# Useful links:
# https://docs.djangoproject.com/en/4.0/topics/db/models/
# https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=5

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Each class will be its own table in the database


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#foreignkey
    # https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
