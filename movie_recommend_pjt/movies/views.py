from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieListSerializers


@api_view(['GET'])
# 영화 전체 조회
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializers(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# 한 영화 디테일 조회
def movie_detail(request):
    pass


# @api_view(['GET'])
# def filter_movie(request):
#     genre_id = request.GET.get('genre')  # 쿼리 파라미터로 장르 ID 받음
#     if not genre_id:
#         return Response({"error": "Genre ID is required"}, status=400)

#     try:
#         # 장르 ID로 영화 필터링
#         movies = Movie.objects.filter(genres__id=genre_id)
#         serializer = MovieListSerializers(movies, many=True)
#         return Response(serializer.data)
#     except Genre.DoesNotExist:
#         return Response({"error": "Invalid Genre ID"}, status=404)
