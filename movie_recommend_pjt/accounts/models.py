from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth = models.DateField()
    study_level = models.CharField(default='A1')
    nickname = models.CharField(max_length=20, unique=True) # 닉네임 중복 방지
    experience = models.IntegerField(default=0)
    achievement_level = models.IntegerField(default=0)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')