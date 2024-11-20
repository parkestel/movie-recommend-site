from django.shortcuts import render
from django.contrib.auth import logout

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from .serializers import CustomUserDetailsSerializer

User = get_user_model()

@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
#  로그인 인증된 사용자만 접근 가능
def profile(request):
    user = request.user
    serializer = CustomUserDetailsSerializer(user)
    return Response(serializer.data)
