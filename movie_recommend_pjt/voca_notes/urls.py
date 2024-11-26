from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/vocanote/create/<int:user_pk>/', views.create_voca_note),
    path('vocanote/list/<int:user_pk>/', views.voca_note_list),
    path('<int:movie_pk>/vocanote/ispublic/<int:user_pk>/', views.change_is_public),
    path('create-voca/<int:vocanote_pk>/', views.create_voca),
    path('vocanote-detail/<int:vocanote_pk>/', views.voca_note_detail),
    path('update-voca/<int:vocanote_pk>/<int:voca_pk>/', views.update_voca),
    path('delete-voca/<int:vocanote_pk>/<int:voca_pk>/', views.delete_voca), 
    path('<int:vocanote_pk>/is_memorized/<int:voca_pk>/', views.change_is_memorized), 
]
