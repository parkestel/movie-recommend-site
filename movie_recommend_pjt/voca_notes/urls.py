from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/vocanote/create/<int:user_pk>/', views.create_voca_note),
    path('<int:movie_pk>/vocanote/list/<int:user_pk>/', views.voca_note_list)
]
