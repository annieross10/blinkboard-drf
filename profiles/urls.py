from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('likes/', views.LikeList.as_view()),
    path('followers/', views.FollowerList.as_view()),
]

