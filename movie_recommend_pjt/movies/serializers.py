from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import Movie, Genre, Star, Ott, Director, Comment

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

# 로그인한 유저의 좋아요한 영화 목록
class WishMovieSerializer(serializers.ModelSerializer):
    # has_voca_note = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['id', 'tmdb_id', 'title', 'poster_path',]
    
    # def get_has_voca_note(self, obj):
    #     # 로그인한 유저와 해당 영화가 연결된 voca_note가 있는지 확인
    #     login_user = self.context.get('request').user
    #     # 해당 영화에 연결된 voca_notes에서 로그인한 유저가 있는지 확인
    #     return obj.voca_notes.filter(users=login_user).exists()
    

# 로그인한 유저의 좋아요한 영화 목록 중 vocanote 없는
class WishMovieVocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'tmdb_id', 'title', 'poster_path']
    


## 코멘트 관련 serializer 시작
class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title',]



# 코멘트 생성
class CommentSerializer(serializers.ModelSerializer):
    movies = MovieCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('users', 'liked_users',)



# 코멘트 영화별 조회 
class CommentListSerializer(serializers.ModelSerializer):
    liked_user_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment 
        fields = ['id', 'users','content', 'liked_user_count', 'liked_users']
        # 코멘트 총 개수, 코멘트 pk, 어떤 유저가 쓴 comment인지, 내용, 코멘트 좋아한 유저들
    
    def get_liked_user_count(self, obj):
    # 각 댓글의 liked_users 수를 반환 (없으면 0)
        return obj.liked_users.count()



# 코멘트 로그인유저별 조회
class CommentUserListSerializer(serializers.ModelSerializer):
    movies = MovieCommentSerializer(read_only=True, many=True)
    liked_user_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'movies', 'liked_user_count', 'liked_users']
        read_only_fields = ('liked_users',)
    def get_liked_user_count(self, obj):
        # 각 코멘트의 liked_users 수 반환 (없으면 0)
        return obj.liked_users.count()



# 로그인 유저의 좋아요한 코멘트 조회
class CommentUserLikedSerializer(serializers.ModelSerializer):
    movies = MovieCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'movies', 'liked_users']
        read_only_fields = ('liked_users',)




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
    

