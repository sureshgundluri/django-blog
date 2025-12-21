from django.urls import path
from .views import *
urlpatterns = [
    path('<int:category_id>/',post_by_category,name='post_by_category')
]
