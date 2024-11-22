from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Voca, VocaNote, Movie

User = get_user_model()

# 단어장 생성
class VocaNoteSerializers(serializers.ModelSerializer):
    class MovieVocaNoteSerializers(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'title']
    movies = MovieVocaNoteSerializers(read_only=True, many=True)
    class Meta:
        model = VocaNote
        fields = '__all__'


class VocaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Voca
        fields = '__all__'


# 단어 생성 & 해당 단어장에 대한 모든 정보
class VocaNoteAllSerializers(serializers.ModelSerializer):
    class MovieVocaNoteSerializers(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'title',]
    movies = MovieVocaNoteSerializers(read_only=True, many=True)
    vocas = VocaSerializers(read_only=True, many=True)

    class Meta:
        model = VocaNote
        fields = '__all__'