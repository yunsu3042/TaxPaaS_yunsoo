from django.db import models

__all__ = ('Ten99', )


class Ten99(models.Model):
    fields = models.CharField(max_length=30)
