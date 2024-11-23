from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.decorators import (
    authentication_classes,
    api_view,
    permission_classes,
)
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from .serializers import PersonUserDetailsSerializer, CustomUserDetailsSerializer
from .serializers import CustomUserUpdateSerializer, CustomUserLevelUpdateSerializer

User = get_user_model()


@api_view(["GET"])
def login_user_data(request):
    user = request.user
    serializer = CustomUserDetailsSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
#  특정 사용자의 프로필 정보 조회 API (로그인 인증된 사용자만 접근 가능)
def profile(request, username):
    person = get_object_or_404(User, username=username)
    serializer = PersonUserDetailsSerializer(person)
    return Response(serializer.data)


# 회원 탈퇴 기능 & 로그아웃까지 연동
@api_view(["POST"])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request):
    message = ""
    if request.user.is_authenticated:
        username = request.user.username
        request.user.delete()
        message = {
            "message": f"회원탈퇴가 완료되었습니다. 삭제된 사용자: {username}",
            "status": "success",
        }
        return Response(data=message, status=status.HTTP_204_NO_CONTENT)
    else:
        # 인증되지 않은 경우
        message = {
            "message": "회원탈퇴에 실패했습니다. 사용자가 인증되지 않았습니다.",
            "status": "failure",
        }
        return Response(data=message, status=status.HTTP_401_UNAUTHORIZED)


# 회원정보 변경 (GET으로 보내면 기존 회원정보 조회, PUT으로 보내면 변경된 정보 조회)
class CustomUserUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """현재 사용자의 모든 정보를 반환"""
        user = request.user
        data = {
            "id": user.id,
            "username": user.username,
            "nickname": user.nickname,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "study_level": user.study_level,
            "birth": user.birth,
            "experience": user.experience,
            "achievement_level": user.achievement_level,
        }
        return Response(data)

    def put(self, request):
        """사용자가 수정 가능한 필드만 업데이트하고 모든 정보를 반환"""
        user = request.user

        # 수정 가능한 필드만 처리
        serializer = CustomUserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            # 모든 사용자 정보를 포함하는 응답 생성
            data = {
                "id": user.id,
                "username": user.username,
                "nickname": user.nickname,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "study_level": user.study_level,
                "birth": user.birth,
                "experience": user.experience,
                "achievement_level": user.achievement_level,
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 유저 study_level
class CustomUserLevelUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """현재 사용자 특정 정보 반환"""
        user = request.user
        data = {
            "id": user.id,
            "username": user.username,
            "nickname": user.nickname,
            "study_level": user.study_level,
        }
        return Response(data)

    def put(self, request):

        user = request.user

        # 수정 가능한 필드만 처리
        serializer = CustomUserLevelUpdateSerializer(
            user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()

            # 모든 사용자 정보를 특정 정보 응답 생성
            data = {
                "id": user.id,
                "username": user.username,
                "nickname": user.nickname,
                "study_level": user.study_level,
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 팔로잉 기능
@api_view(["POST"])
def followings(request, user_pk):
    person = User.objects.get(pk=user_pk)
    me = request.user
    if me != person:
        if me in person.followers.all():
            # 팔로잉 취소
            person.followers.remove(me)
            return Response(
                {"status": "following 취소", "끊은 person": person.nickname},
                status=status.HTTP_200_OK,
            )
        else:
            # 팔로잉 추가
            person.followers.add(me)
            return Response(
                {"status": "following", "followings": person.nickname},
                status=status.HTTP_200_OK,
            )
    else:
        return Response(
            {"error": "자기 자신을 팔로우할 수 없습니다."},
            status=status.HTTP_400_BAD_REQUEST,
        )
