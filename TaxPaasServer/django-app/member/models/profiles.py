from django.db import models
from taxpaas.settings import AUTH_USER_MODEL

__all__ = ('TaxPayerProfile', 'TaxPractitionerProfile', 'Connection')


class TaxPayerProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL)
    organizer = models.OneToOneField('taxorg.TaxOrganizer', null=True, blank=True)
    img = models.ImageField(upload_to="profile/payer", null=True, blank=True)

    def __str__(self):
        return self.user.email + "_tax payer"


class TaxPractitionerProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL)
    is_certificated = models.BooleanField(default=False)
    locals = models.CharField(max_length=100)
    clients = models.ManyToManyField(TaxPayerProfile, through='Connection',
                                     blank=True)
    img = models.ImageField(upload_to="profile/practitioner", blank=True,
                            null=True)

    def __str__(self):
        return self.user.name + "_tax practitioner"


class Connection(models.Model):
    tax_practitioner = models.ForeignKey(TaxPractitionerProfile)
    tax_payer = models.ForeignKey(TaxPayerProfile)
    joined_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    task = models.CharField(max_length=500, blank=True)