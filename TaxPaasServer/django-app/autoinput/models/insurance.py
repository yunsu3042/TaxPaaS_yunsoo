from django.db import models

__all__ = ('Ten95B', 'Ten95C')


class Ten95B(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    ssn = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)


class Ten95C(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    city = models.CharField(max_length=30, blank=True)
    ssn = models.CharField(max_length=30, blank=True)

