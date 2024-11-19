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

@api_view(['POST'])
# 사용자 인증토큰 삭제
def custom_logout(request):
    # 사용자 인증 여부 확인
    if not hasattr(request.user, 'auth_token'):
        return Response({"detail": "유효하지 않은 토큰이거나 사용자 인증이 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.auth_token.delete() # 토큰 삭제
    logout(request) # 세션 종료
    return Response({"detail": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
#  로그인 인증된 사용자만 접근 가능
def profile(request):
    user = request.user
    serializer = CustomUserDetailsSerializer(user)
    return Response(serializer.data)
