from django.db import models
from django.conf import settings


# Create your models here.
class Star(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    name_kr = models.TextField()
    profile_path = models.TextField(null=True, blank=True)
    characters = models.JSONField()


class Ott(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    logo_path = models.TextField()
    site_url = models.TextField()


class Genre(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=20)


class Director(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    profile_path = models.TextField(null=True, blank=True)


class Movie(models.Model):
    tmdb_id = models.IntegerField()  # id
    title = models.TextField()  # title
    title_kr = models.TextField()
    rank = models.FloatField()  # vote_average
    release_date = models.DateField()  # release_date
    runtime = models.IntegerField()
    summary = models.TextField()  # overview
    production = models.TextField()
    country = models.TextField()
    poster_path = models.TextField()  # poster_path
    is_adult = models.BooleanField()  # adult
    difficulty = models.TextField()
    stars = models.ManyToManyField(Star, related_name="stared_movie")
    genres = models.ManyToManyField(Genre, related_name="included_movies")
    otts = models.ManyToManyField(Ott, related_name="provide_movies")
    directors = models.ManyToManyField(Director, related_name="directed_movies")
    wish_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="wish_movies"
    )


class Comment(models.Model):
    content = models.TextField()
    movies = models.ManyToManyField(Movie, related_name="comments")
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="user_comments"
    )
    liked_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_comments"
    )


# 좋아요 경험치 로직 떄문에 추가한 모델
class CommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # 좋아요를 누른 시간 기록

    class Meta:
        unique_together = ("user", "comment")


# 위시무비 담을 때 경험치 로직
class WishMovieHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
