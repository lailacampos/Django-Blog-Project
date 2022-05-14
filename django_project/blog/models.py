# Useful links:
# https://docs.djangoproject.com/en/4.0/topics/db/models/
# https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=5
# https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=10

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.

# Each class will be its own table in the database


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_img', blank=True)

    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#foreignkey
    # https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.name)
    #
    #     # Resizing the image if larger than wanted:
    #     if img.height > 500 or img.width > 500:
    #         output_size = (500, 500)
    #         img.thumbnail(output_size)
    #         img.save(self.image.name)
