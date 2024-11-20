from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies),
    path('movies/detail/', views.movie_detail),
]
