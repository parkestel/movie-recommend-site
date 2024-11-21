from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from django.contrib.auth import get_user_model
from movies.serializers import WishMovieSerializer

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    birth = serializers.DateField()
    study_level = serializers.CharField(max_length=10)
    nickname = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]  # 고유성 검사 추가
    )
    first_name = serializers.CharField(max_length=30)  # 추가
    last_name = serializers.CharField(max_length=30)   # 추가

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'last_name': self.validated_data.get('last_name', ''),    # 추가
            'first_name': self.validated_data.get('first_name', ''),  # 추가
            'email': self.validated_data.get('email', ''),
            'birth': self.validated_data.get('birth', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'study_level': self.validated_data.get('study_level', 'A1'),
        }

    def save(self, request):
        user = super().save(request)
        user.last_name = self.validated_data.get('last_name')    # 추가
        user.first_name = self.validated_data.get('first_name')  # 추가
        user.birth = self.validated_data.get('birth')
        user.nickname = self.validated_data.get('nickname')
        user.study_level = self.validated_data.get('study_level')
        user.save()
        return user

class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True)
    email = None


class FollowSerializer(serializers.ModelSerializer):
    """
    followings/followers 필드를 위한 서브 직렬화
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'nickname']  # 필요한 필드만 포함

# 현재 로그인 한 사용자 정보 반환
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = User
        # id == pk 값
        fields = [
            'id', 'nickname', 'username'
        ]
        read_only_fields = ['id', 'username','nickname']  # 읽기 전용 필드


# 특정 사용자 조회
class PersonUserDetailsSerializer(UserDetailsSerializer):
    followings = FollowSerializer(many=True, read_only=True)
    followers = FollowSerializer(many=True, read_only=True)
    wish_movies = WishMovieSerializer(many=True, read_only=True)
    class Meta:
        model = User
        # id == pk 값
        fields = [
            'id', 'nickname','study_level', 'experience', 
            'achievement_level', 'followings', 'followers', 'wish_movies'
        ]
        read_only_fields = ['id', 'followings', 'followers']  # 읽기 전용 필드

