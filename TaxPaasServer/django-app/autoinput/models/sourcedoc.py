from django.db import models

__all__ = ('SourceDoc', )

CATEGORY_CHOICE = (('M', 'Mine'),
                   ('S', 'Spouse'),
                   ('D', 'Dependents'),)


class SourceDoc(models.Model):
    tax_payer = models.ForeignKey('member.TaxPayerProfile', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)

    def __str__(self):
        return self.category
