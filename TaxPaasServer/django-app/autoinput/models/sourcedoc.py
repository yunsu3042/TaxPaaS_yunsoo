from django.db import models
from member.models import TaxPayerProfile
__all__ = ('SourceDoc', )

CATEGORY_CHOICE = (('M', 'Mine'),
                   ('S', 'Spouse'),
                   ('C', 'Child'),)


class SourceDoc(models.Model):
    user = models.ForeignKey('member.TaxPayerProfile', blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICE,
                                null=True, blank=True)

    def __str__(self):
        return self.category