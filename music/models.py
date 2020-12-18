from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    path_to_file = models.FileField(upload_to='static/')
    favorite_by = models.ManyToManyField(User, related_name='favourite_songs')
