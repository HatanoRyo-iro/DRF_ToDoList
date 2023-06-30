from django.shortcuts import render
from rest_framework import viewsets

from .models import ToDoItem
from .serializers import ToDoItemSerializer

# Create your views here.

class ToDoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer