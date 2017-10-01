from django.db import models

__all__ = ('SourceDoc', )


class SourceDoc(models.Model):
    w2 = models.ForeignKey('autoinput.W2')
    ten99 = models.ForeignKey('autoinput.Ten99')
    interest = models.ForeignKey('autoinput.Interest')
    dividend_income = models.ForeignKey('autoinput.DividendIncome')