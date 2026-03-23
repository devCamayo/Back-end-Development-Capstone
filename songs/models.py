from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    year = models.IntegerField()
    lyrics = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.title} - {self.artist}'
