from django.db import models

__all__ = ('Ten99INT', 'Ten99DIV', 'Ten98', 'Ten95B', 'Ten95C')


class Ten99INT(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    fields = models.CharField(max_length=30, blank=True)
    interest_income = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)


class Ten99DIV(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    qualified_dividends = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)


class Ten98(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    mortgage_interest = models.CharField(max_length=30, blank=True)
    refund = models.CharField(max_length=30, blank=True)


class Ten95B(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    ssn = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)


class Ten95C(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    city = models.CharField(max_length=30, blank=True)
    ssn = models.CharField(max_length=30, blank=True)
