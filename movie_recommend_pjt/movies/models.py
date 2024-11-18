from django.db import models

# Create your models here.
class Star(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    profile_path = models.TextField()
    characters = models.JSONField()
    