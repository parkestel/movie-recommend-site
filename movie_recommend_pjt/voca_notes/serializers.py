from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Voca, VocaNote, Movie

User = get_user_model()

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