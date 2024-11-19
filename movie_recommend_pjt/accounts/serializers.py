from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname','username', 'first_name', 'last_name', 'email', 
                  'birth', 'password','study_level')
        extra_kwargs = {
            'password': {'write_only': True},  # 비밀번호를 쓰기 전용으로 설정
        }

        def create(self, validated_data):
            user = User(
                username=validated_data['username'],
                first_name=validated_data.get('first_name'),
                last_name=validated_data.get('last_name'),
                email=validated_data['email'],
                birth=validated_data.get('birth'),
                nickname=validated_data['nickname'],
                study_level=validated_data.get('study_level'),
            )
            user.set_password(validated_data['password'])
            user.save()
            return user