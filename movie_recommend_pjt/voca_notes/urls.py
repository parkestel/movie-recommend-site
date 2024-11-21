from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/vocanote/create/<int:user_pk>/', views.create_voca_note),
    path('vocanote/list/<int:user_pk>/', views.voca_note_list),
    path('<int:movie_pk>/vocanote/ispublic/<int:user_pk>/', views.change_is_public)
]
