from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('category/view/', viewCategory, name='viewCategory'),
    path('task/view/<str:id>/', viewTask, name='viewTask'),
    path('category/update/<str:id>/', updateCategory, name='updateCategory'),
    path('task/update/<str:id>/', updateTask, name='updateTask'),
    path('task/edit/<str:id>/',editTask,name='editTask')
]