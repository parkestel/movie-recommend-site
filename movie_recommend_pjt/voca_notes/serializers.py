from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Voca, VocaNote

User = get_user_model()

class VocaNoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = VocaNote
        fields = '__all__'

class VocaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Voca
        fields = '__all__'