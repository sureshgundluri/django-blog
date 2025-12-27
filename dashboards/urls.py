from django.urls import path
from .views import *
urlpatterns =[
    path('',dashboards,name='dashboards'),
    # Category
    path('categories/',categories,name='categories'),
    path('categories/add/',add_category,name='add_category'),
    path('categories/edit/<int:pk>/',edit_category,name='edit_category'),
    path('categories/delete/<int:pk>/',delete_category,name='delete_category'),

    # Blog Post Cards
    path('posts/',posts,name='posts'),
    path('posts/add/',add_post,name='add_post'),
    path('posts/edit/<int:pk>/',edit_post,name='edit_post'),
    path('posts/delete/<int:pk>/',delete_post,name='delete_post'),

    # Users

    path('users/',users,name='user'),
    path('users/add',add_user,name='add_user'),
    path('users/edit/<int:pk>/',edit_user,name='edit_user'),
    path('user/delete/<int:pk>/',delete_user,name='delete_user'),
]