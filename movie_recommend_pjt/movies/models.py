from django.db import models

# Create your models here.
class Star(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    profile_path = models.TextField()
    characters = models.JSONField()

class Ott(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    logo_path = models.TextField()

class Genre(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=20)