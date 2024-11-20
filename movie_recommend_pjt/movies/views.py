from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieListSerializers


@api_view(['GET'])
# 영화 전체 조회
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializers(movies, many=True)
    return Response(serializer.data)


# 영화 좋아요 눌렀을 때 내 프로필 페이지에서 wish_movies 볼 수 있게 vue에서 버튼 누르면 저장시키는 로직
@api_view(['POST'])
def wish_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if movie.wish_users.filter(id=user.id).exists():
        # 이미 좋아요를 눌렀으면 취소
        movie.wish_users.remove(user)
        return Response({'status': 'removed', 'movie_pk': movie_pk}, status=status.HTTP_200_OK)
    else:
        # 좋아요 추가
        movie.wish_users.add(user)
        return Response({'status': 'added', 'movie_pk': movie_pk}, status=status.HTTP_200_OK)


