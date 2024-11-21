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
        fields = ['id', 'tmdb_id', 'title', 'poster_path']

# 메인페이지 전체 영화 조회
class MovieListSerializers(serializers.ModelSerializer):

    genres = GenreListSerializers(many=True, read_only=True)
    stars = StarListSerializers(many=True, read_only=True)
    otts = OttListSerializers(many=True, read_only=True)
    directors = DirectorListSerializers(many=True, read_only=True)
    liked_user = serializers.SerializerMethodField() # 현재 로그인한 유저가 좋아요했는지 안했는지 여부

    class Meta:
        model = Movie
        fields = '__all__'
        
    def get_liked_user(self, obj):
        # 로그인한 유저를 가져옵니다.
        user = self.context.get('request').user
        
        # 로그인한 유저가 해당 영화에 좋아요를 눌렀다면 유저의 pk를 반환
        if user in obj.wish_users.all():  # wish_users에 로그인한 유저가 포함되어 있는지 확인
            return user.pk
        return None  # 좋아요를 누르지 않았다면 None을 반환
