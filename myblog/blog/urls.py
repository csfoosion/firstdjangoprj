from django.urls import path
from django.urls.conf import include
from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #127.0.0.1:8000/post/1 패턴에 해당하는 path
    #/post/숫자/ 를 2차 url로 작성 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
]