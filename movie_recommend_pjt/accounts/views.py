from django.shortcuts import render
from django.contrib.auth import get_user_model

from .serializers import CustomUserSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

User = get_user_model()

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def signup(request):
    serialized = CustomUserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)