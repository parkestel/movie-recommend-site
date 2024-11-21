from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/vocanote/<int:user_pk>/', views.create_voca_note)
]
