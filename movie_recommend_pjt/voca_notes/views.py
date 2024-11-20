from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import VocaNoteListSerializers
from .models import VocaNote, Voca
from movies.models import Movie

User = get_user_model()

# create(내 단어장 로그인한 사용자랑 pk확인), read(다른 사람들 단어장 읽는), update(내 단어장 로그인한 사용자랑 pk확인), delete(내 단어장 로그인한 사용자랑 pk확인)

# Vocanote 생성 : 보는 사람이랑 로그인한 사용자랑 같아야 단어장 생성 가능.
@api_view('POST', 'DELETE') 
def create_voca_note(request, movie_pk, user_pk):
    movie = Movie.objects.get(pk=movie_pk)
    person = User.objects.get(pk=user_pk)
    me = request.user

    if me == person:
        serializer = VocaNoteListSerializers(근데,,,,그거 어떻게 해 )
        # 나니까 단어장 자동 생성
        # vocanote 하나 만들어질 때, 
        # if 근데 이미 이 영화에 단어장있으면 못만들어 디버깅 메세지 
        pass
    else:
        return Response('다른 사람 단어장은 생성할 수 없습니다.')


# 단어장 보여주기만
@api_view(['GET'])
def voca_note_list(request):
    pass