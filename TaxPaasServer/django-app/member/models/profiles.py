from django.db import models
from taxpaas.settings import AUTH_USER_MODEL

__all__ = ('TaxPayerProfile', 'TaxPractitionerProfile', 'Connection')


class TaxPayerProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL)
    organizer = models.ForeignKey('taxorg.TaxOrganizer')
    my_source_doc = models.ForeignKey(
        'autoinput.SourceDoc', related_name='my_source_doc_set')
    spouse_source_doc = models.ForeignKey(
        'autoinput.SourceDoc', related_name='spouse_source_doc_set')
    children_source_doc = models.ForeignKey(
        'autoinput.SourceDoc', related_name='children_source_doc_set')

    def __str__(self):
        return self.user.name + "_tax payer"


class TaxPractitionerProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL)
    is_certificated = models.BooleanField(default=False)
    locals = models.CharField(max_length=100)
    clients = models.ManyToManyField(TaxPayerProfile, through='Connection')

    def __str__(self):
        return self.user.name + "_tax practitioner"


class Connection(models.Model):
    tax_practitioner = models.ForeignKey(TaxPractitionerProfile)
    tax_payer = models.ForeignKey(TaxPayerProfile)
    joined_date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=1000, blank=True)
    task = models.CharField(max_length=500, blank=True)