from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Voca, VocaNote

User = get_user_model()

class VocaNoteListSerializers(serializers.ModelSerializer):
    class Meta:
        model = VocaNote
        fields = '__all__'