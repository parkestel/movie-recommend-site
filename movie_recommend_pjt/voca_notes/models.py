from django.db import models
from movies.models import Movie
from django.conf import settings


# Create your models here.
class Voca(models.Model):
    word = models.TextField()
    word_mean = models.TextField()
    examples = models.TextField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    is_memorized = models.BooleanField(default=False)
    was_memorized = models.BooleanField(default=False)


class VocaNote(models.Model):
    is_public = models.BooleanField(default=True)
    movies = models.ManyToManyField(Movie, related_name="voca_notes")
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="voca_notes")
    vocas = models.ManyToManyField(Voca, related_name="voca_notes")

# 영화별 단어장 생성 기록을 관리하는 모델
class VocaNoteHistory(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'user')  # 같은 영화에 대해 한 명의 사용자만 단어장을 생성할 수 있도록 유니크 제약

