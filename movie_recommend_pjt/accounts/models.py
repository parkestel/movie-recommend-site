from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth = models.DateField(blank=True, null=True) # 기존 데이터와 호환..
    study_level = models.CharField(max_length=5, default='A1')
    nickname = models.CharField(max_length=20, unique=True) # 닉네임 중복 방지
    experience = models.IntegerField(default=0)
    achievement_level = models.IntegerField(default=1)
    percent = models.FloatField(default=0)  # percent 필드 추가
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def save(self, *args, **kwargs):
        """
        `experience`가 업데이트 될 때마다 `achievement_level`과 `percent`를 갱신합니다.
        """
        self.calculate_achievement_level()  # achievement_level 갱신
        self.calculate_percent()  # percent 갱신
        super().save(*args, **kwargs)  # 부모 클래스 save 호출 (DB에 저장)

    def calculate_achievement_level(self):
        """
        experience에 따라 achievement_level을 갱신
        """
        if self.experience < 1000:
            self.achievement_level = 1
        elif self.experience < 3000:
            self.achievement_level = 2
        elif self.experience < 6000:
            self.achievement_level = 3
        else:
            self.achievement_level = 4

    def calculate_percent(self):
        """
        `achievement_level`에 맞는 레벨 구간에서 현재 경험치가 채운 퍼센트를 계산
        """
        level_thresholds = {
            1: (0, 999),
            2: (1000, 2999),
            3: (3000, 5999),
            4: (6000, float('inf'))  # 무한대, 6000 이상은 레벨 4
        }

        level_min, level_max = level_thresholds.get(self.achievement_level, (0, 0))

        # 현재 레벨 구간에 맞는 퍼센트 계산
        if level_max > level_min:
            progress = (self.experience - level_min) / (level_max - level_min) * 100
        else:
            progress = 100  # 레벨 4 이상일 경우, 경험치가 무한대이므로 100% 처리

        self.percent = round(progress, 2)