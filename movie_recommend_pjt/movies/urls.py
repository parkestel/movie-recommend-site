from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies),
    path('movies/<movie_pk>/wish-movie/', views.wish_movie),
    path('movies/wish-movie/', views.logined_wish_movie_list),
]
