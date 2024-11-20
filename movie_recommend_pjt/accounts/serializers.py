from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from django.contrib.auth import get_user_model

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
            'study_level': self.validated_data.get('study_level', ''),
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

# 사용자 조회
class CustomUserDetailsSerializer(UserDetailsSerializer):
    followings = FollowSerializer(many=True, read_only=True)
    followers = FollowSerializer(many=True, read_only=True)

    class Meta:
        model = User
        # id == pk 값
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'nickname',
            'birth', 'study_level', 'experience', 'achievement_level', 'followings', 'followers'
        ]
        read_only_fields = ['email', 'id', 'followings', 'followers']  # 읽기 전용 필드

# class CustomAccountAdapter(DefaultAccountAdapter):
#     def save_user(self, request, user, form, commit=True):
#         """
#         사용자 데이터를 저장할 때 커스텀 처리
#         """
#         data = form.cleaned_data
#         first_name = data.get("first_name")
#         last_name = data.get("last_name")
#         email = data.get("email")
#         username = data.get("username")
#         nickname = data.get("nickname")
#         birth = data.get("birth")
#         study_level = data.get("study_level")
#         experience = data.get("experience", 0)
#         achievement_level = data.get("achievement_level", 0)

#         user_email(user, email)
#         user_username(user, username)
#         if first_name:
#             user_field(user, "first_name", first_name)
#         if last_name:
#             user_field(user, "last_name", last_name)
#         if nickname:
#             user_field(user, "nickname", nickname)
#         if birth:
#             user_field(user, "birth", birth)
#         if study_level:
#             user_field(user, "study_level", study_level)
#         if experience:
#             user_field(user, "experience", experience)
#         if achievement_level:
#             user_field(user, "achievement_level", achievement_level)
#         if "password1" in data:
#             user.set_password(data["password1"])
#         else:
#             user.set_unusable_password()
#         self.populate_username(request, user)
#         if commit:
#             user.save()
#         return user