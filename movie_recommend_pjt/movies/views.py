from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Movie, Genre, Ott, Comment
from .serializers import MovieListSerializers, WishMovieSerializer, OttListSerializers, GenreListSerializers
from .serializers import CommentSerializer, CommentListSerializer, CommentUserListSerializer

User = get_user_model()

# 영화 전체 조회
@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializers(movies, many=True, context={'request': request})
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

# 로그인 한 유저가 좋아요 한 영화 목록
@api_view(['GET'])
def logined_wish_movie_list(request):
    login_user = request.user
    wished_movies = Movie.objects.filter(wish_users=login_user)

    serializer = WishMovieSerializer(wished_movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genres_list(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializers(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def otts_list(request):
    otts = Ott.objects.all()
    serializer = OttListSerializers(otts, many=True)
    return Response(serializer.data)

# 코멘트 생성
@api_view(['POST', 'PUT'])
def comment_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # movies, users iterable이기 때문에 단일 객체 리스트 형태로[]로 감싸줘야함
            serializer.save(movies=[movie], users=[request.user])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 유저가 작성한 comment 조회
@api_view(['GET','DELETE'])
def comment_list_user(request, comment_pk):
    login_user = request.user

    if request.method == 'GET':
        # 유저가 작성한 모든 영화에 따른 코멘트 내용들 
        comments = Comment.objects.filter(users=login_user)
        serializer = CommentUserListSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        comment = Comment.objects.filter(pk=comment_pk, users=login_user).first()
        if comment:
            comment.delete()

            print(f"Deleting comment with ID: {comment.pk}, Content: {comment.content}")

            # 삭제 후 유저가 작성한 모든 영화 다시 조회
            comments = Comment.objects.filter(users=login_user)
            serializer = CommentUserListSerializer(comments, many=True)
            return Response({
                    'message': f"Comment with ID {comment.pk} has been deleted.",
                    'remaining_comments': serializer.data
                }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': '삭제할 코멘트가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

# 영화별 코멘트 조회
@api_view(['GET', 'DELETE'])
def comment_list_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = Comment.objects.filter(movies=movie)
    serializer = CommentListSerializer(comments, many=True)

    # 해당 영화에 대한 총 코멘트 수
    total_comments = comments.count()

    return Response({
        'number_of_count': total_comments,  # 총 코멘트 개수
        'comments': serializer.data  # 코멘트 목록
    }, status=status.HTTP_200_OK)

# @api_view(['DELETE'])
# def comment_delete(request, comment_pk):
#     login_user = request.user
#     comment = Comment.objects.get(pk=comment_pk)
#     if comment.users == login_user.pk:
#         comment.delete()
#         return Response()