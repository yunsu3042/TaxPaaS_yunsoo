from django.db import models

__all__ = ('Dependents', 'DetailDependentInfo')

class Dependents(models.model):
    dependentQ1 = models.BooleanField(default=False)
    dependentQ2 = models.BooleanField(default=False)
    dependentQ3 = models.BooleanField(default=False)
    dependentQ4 = models.BooleanField(default=False)
    dependentQ5 = models.BooleanField(default=False)
    dependentQ6 = models.BooleanField(default=False)
    dependentQ7 = models.BooleanField(default=False)
    dependentQ8 = models.BooleanField(default=False)
    dependentQ9 = models.BooleanField(default=False)
    dependentQ10 = models.BooleanField(default=False)
    dependentQ11 = models.BooleanField(default=False)
    dependentQ12 = models.BooleanField(default=False)
    dependentQ13 = models.BooleanField(default=False)
    dependentQ14 = models.BooleanField(default=False)
    dependentQ15 = models.BooleanField(default=False)
    dependentQ16 = models.BooleanField(default=False)
    dependentQ17 = models.BooleanField(default=False)
    dependentQ18 = models.BooleanField(default=False)
    dependentQ19 = models.BooleanField(default=False)

class DetailDependentInfo(models.model):
    dependents = models.ForeignKey(Dependents,, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,blank=True)
    relationship = models.CharField(max_length=30,blank=True)
    dOB = models.DateField(input_formats=settings.DATE_INPUT_FORMATS) #DateOfBirth
    sSN = models.CharField(max_length=30,blank=True)
    mLWY = models.CharField(max_length=10,blank=True) #monthsLivedWithYou
    disabled = models.BooleanField(default=False)
    fTS = models.models.BooleanField(default=False) #full time student
    dFI = models.BooleanField(default=False) #Dependent's Gross Income


