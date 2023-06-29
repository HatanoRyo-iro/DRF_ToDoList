from django.db import models

import uuid

# Create your models here.

class ToDoItem(models.Model):
    
    class Meta:
        db_table = "todo_item"
        ordering = ["created_at"]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='Title', max_length=100)
    content = models.TextField(verbose_name='Content', blank=True, null=True)
    completed = models.BooleanField(verbose_name='Completed', default=False)
    created_at = models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    
    def __str__(self):
        return self.title