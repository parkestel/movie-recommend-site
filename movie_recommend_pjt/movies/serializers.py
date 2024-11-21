from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import Movie, Genre, Star, Ott, Director

User = get_user_model()

# 장르
class GenreListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# 배우
class StarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'

# ott
class OttListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ott
        fields = '__all__'

# 감독
class DirectorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

# wish_movies
class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = ['id', 'nickname']  # 필요한 필드만 포함

class WishMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'tmdb_id', 'title']

# 한번에 넘길 무비 관련 모든 정보
class MovieListSerializers(serializers.ModelSerializer):

    genres = GenreListSerializers(many=True, read_only=True)
    stars = StarListSerializers(many=True, read_only=True)
    otts = OttListSerializers(many=True, read_only=True)
    directors = DirectorListSerializers(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
