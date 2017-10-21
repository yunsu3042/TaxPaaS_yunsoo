from django.db import models

__all__ = ('PersonalInfo', 'DetailPersonalInfo')

class PersonalInfo(models.model):
    streetAddr = models.CharField(max_length = 200,blank=True)
    city = models.CharField(max_length = 50,blank=True)
    stste = models.USStateField(widget=USStateSelect, required=False)
    zipCode = models.USZipCodeField(blank=True, null=True)
    homePhone = models.PhoneNumberField(blank=True)
    MARITALSTATUS_CHOICES = (
    (u'1', u'Married'),
    (u'2', u'Single'),
    (u'3', u'Wodiw(er)'),
    )
    maritalStatus = models.CharField(max_length=1, choices=MARITALSTATUS_CHOICES)
    #if (MARITALSTATUS_CHOICES=='3')
    dateOfSpouseDeath = DateField(input_formats=settings.DATE_INPUT_FORMATS, blank=True)

class DetailPersonalInfo(models.model): #1. Personal Information
    personalInfo = models.ForeignKey(PersonalInfo,, on_delete=models.CASCADE)
    SELECTPERSON_CHOICES = (
    (u'1', u'Taxpayer'),
    (u'2', u'Spouse'),
    )
    selectPerson = models.CharField(max_length=1, choices=SELECTPERSON_CHOICES)
    name = models.CharField(max_length=30,blank=True)
    sSN = models.CharField(max_length=30,blank=True)
    dOB = models.DateField(input_formats=settings.DATE_INPUT_FORMATS) #DateOfBirth
    oCP = models.CharField(max_length=30,blank=True) #Occupation
    wP = models.models.PhoneNumberField(blank=True) #WorkPhone
    blind = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    presCampaignedFund = models.BooleanField(default=False)


