from django.urls import path
from .views import *
urlpatterns =[
    path('',dashboards,name='dashboards'),
    path('categories/',categories,name='categories'),
    path('categories/add/',add_category,name='add_category'),
    path('categories/edit/<int:pk>/',edit_category,name='edit_category'),
    path('categories/delete/<int:pk>/',delete_category,name='delete_category')
]
