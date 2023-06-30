from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('todo', views.ToDoItemViewSet)

app_name = 'todo'
urlpatterns = [
    path('', include(router.urls)),
]