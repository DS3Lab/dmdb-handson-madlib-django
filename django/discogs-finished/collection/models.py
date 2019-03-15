from django.db import models
from datetime import datetime

# Create your models here.

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    realname = models.TextField(null=True, blank=True)
    profile = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return '(%d) %s' % (self.artist_id, self.name)

class Release(models.Model):
    release_id = models.AutoField(primary_key=True)
    released = models.DateTimeField(default=datetime.now)
    title = models.TextField()
    country = models.CharField(max_length=256, null=True, blank=True)
    genre = models.CharField(max_length=256, null=True, blank=True)
    
    artists = models.ManyToManyField(Artist)
    
    def __str__(self):
        return '(%d) %s' % (self.release_id, self.title)

class Track(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    track_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=128)
    title = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    
    def __str__(self):
        return '(%d) %s' % (self.track_id, self.title)
    

