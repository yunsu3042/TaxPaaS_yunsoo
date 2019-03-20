from django.db import models

__all__ = ('TaxOrganizer', )


class TaxOrganizer(models.Model):
    personal_info = models.CharField(max_length=20, blank=True)


