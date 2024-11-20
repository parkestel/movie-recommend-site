from django.shortcuts import render
from django.contrib.auth import logout

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
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
    try:
        user = request.user
        if not user.is_authenticated:
                raise AuthenticationFailed("인증되지 않은 사용자입니다.")
        serializer = CustomUserDetailsSerializer(user)
        return Response(serializer.data)
    except AuthenticationFailed as e:
        return Response(
            {"detail": str(e), "status": "failed"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    except Exception as e:
        # 기타 예외 처리
        return Response(
            {"detail": "서버 오류가 발생했습니다.", "error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# 회원 탈퇴 기능 & 로그아웃까지 연동
@api_view(['POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request):
    message = ''
    if request.user.is_authenticated:
        username = request.user.username
        request.user.delete()
        message = {
            "message": f"회원탈퇴가 완료되었습니다. 삭제된 사용자: {username}",
            "status": "success"
        }
        return Response(data=message, status=status.HTTP_204_NO_CONTENT)
    else:
        # 인증되지 않은 경우
        message = {
            "message": "회원탈퇴에 실패했습니다. 사용자가 인증되지 않았습니다.",
            "status": "failure"
        }
        return Response(data=message, status=status.HTTP_401_UNAUTHORIZED)
    
# 팔로잉 기능
@api_view(['POST'])
def followings(request, user_pk):
    person = User.objects.get(pk=user_pk)
    me = request.user
    if me != person:
        if me in person.followers.all():
            # 팔로잉 취소
            person.followers.remove(me)
            return Response({'status': 'following 취소', '끊은 person': person.nickname}, status=status.HTTP_200_OK)
        else:
            # 팔로잉 추가
            person.followers.add(me)
            return Response({'status': 'following', 'followings': person.nickname}, status=status.HTTP_200_OK)
    else:
            return Response({'error': '자기 자신을 팔로우할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    