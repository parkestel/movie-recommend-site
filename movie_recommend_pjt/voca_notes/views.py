from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import VocaNoteSerializers,VocaSerializers
from .models import VocaNote, Voca
from movies.models import Movie

User = get_user_model()

# create(내 단어장 로그인한 사용자랑 pk확인), read(다른 사람들 단어장 읽는), update(내 단어장 로그인한 사용자랑 pk확인), delete(내 단어장 로그인한 사용자랑 pk확인)

# Vocanote 생성 : 보는 사람이랑 로그인한 사용자랑 같아야 단어장 생성 가능.
@api_view('GET','POST', 'DELETE') 
@permission_classes([IsAuthenticated])  # 로그인된 사용자만 접근 가능
def create_voca_note(request, movie_pk, user_pk):

    person = get_object_or_404(User, pk=user_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    me = request.user

    if request.method == 'GET':

        voca_notes = VocaNote.objects.filter(users=person, movies=movie)
        if not voca_notes.exists():
            return Response({'error': '해당 영화에 대한 단어장이 없습니다.'}, status=404)
        
        if person != me and not any(note.is_public for note in voca_notes):
            return Response({'error': '해당 단어장은 비공개 상태입니다.'}, status=403)
        
        serializer = VocaNoteSerializers(voca_notes, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':

        if me != person:
            return Response({'error': '자신의 단어장만 생성할 수 있습니다.'}, status=403)
        

        existing_note = VocaNote.objects.filter(users=me, movies=movie).first()
        if existing_note:
            return Response({'error': '이미 해당 영화에 대한 단어장이 존재합니다.'}, status=400)

        voca_note = VocaNote.objects.create(is_public=True)  # 기본 공개 상태로 생성
        voca_note.users.add(me)
        voca_note.movies.add(movie)
        voca_note.save()

        serializer = VocaNoteSerializers(voca_note)
        return Response(serializer.data, status=201)

    elif request.method == 'DELETE':
        # 삭제 - 로그인한 사용자만 가능
        voca_note = VocaNote.objects.filter(users=me, movies=movie).first()
        if not voca_note:
            return Response({'error': '삭제할 단어장이 존재하지 않습니다.'}, status=404)
        
        voca_note.delete()
        return Response({'message': '단어장이 삭제되었습니다.'}, status=200)



# 단어장 보여주기만
@api_view(['GET'])
def voca_note_list(request):
    pass