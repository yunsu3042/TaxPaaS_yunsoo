from django.db import models

__all__ = ('Task', )


class Task(models.Model):
    # A model to save information about an asynchronous task
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    job_id = models.CharField(max_length=128, primary_key=True)
    result = models.TextField()