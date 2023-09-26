from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=True)
