from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies),
    path('movies/<int:movie_pk>/wish-movie/', views.wish_movie),
    path('movies/wish-movie/', views.logined_wish_movie_list),
    path('movies/wish-movies-without-vocanote/', views.wish_movie_without_vocanote),
    path('movies/genres-list/', views.genres_list),
    path('movies/otts-list/', views.otts_list),
    path('movies/<int:movie_pk>/create-comment/', views.comment_create),
    path('movies/comment-list/user/<int:comment_pk>/', views.comment_list_user),
    path('movies/comment-list/<int:movie_pk>/', views.comment_list_movie),
    path('movies/<int:movie_pk>/comment-update/<int:comment_pk>/', views.update_comment),
]
