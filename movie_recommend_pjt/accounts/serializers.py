from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.serializers import PrimaryKeyRelatedField
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

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        if hasattr(User, 'USERNAME_FIELD'):
            extra_fields.append(User.USERNAME_FIELD)
        if hasattr(User, 'EMAIL_FIELD'):
            extra_fields.append(User.EMAIL_FIELD)
        if hasattr(User, 'STUDY_LEVEL_FIELD'):
            extra_fields.append(User.STUDY_LEVEL_FIELD)    
        if hasattr(User, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(User, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(User, 'nickname'):
            extra_fields.append('nickname')    
        model = User
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)