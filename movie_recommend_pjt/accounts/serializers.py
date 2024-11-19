from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from dj_rest_auth.registration.serializers import RegisterSerializer
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
            'password': self.validated_data.get('password', ''),
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

