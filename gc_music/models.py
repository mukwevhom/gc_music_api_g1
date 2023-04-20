from django.db import models

# Create your models here.
class Song(models.Model):
    songname = models.CharField(max_length=255)
    songartist = models.CharField(max_length=255)
    songimg = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.songartist} - {self.songname}'