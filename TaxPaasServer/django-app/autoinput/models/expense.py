from django.db import models

__all__ = ('Ten99INT', 'Ten99DIV', 'Ten99G', 'Ten99MISC', 'Ten99Mortgage',
           'Ten98EStudentLoanInterest', 'Ten98TTuitionStatement', 'ChildCare')


# 이자소득
class Ten99INT(models.Model):
    img = models.ImageField(upload_to="ten99int")
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    order = models.IntegerField(default=0)
    state = models.CharField(max_length=50, blank=True)
    specified_private_bond = models.CharField(max_length=50, blank=True)
    bond_premium_tax_exempt = models.CharField(max_length=50, blank=True)
    bond_premium = models.CharField(max_length=50, blank=True)
    payer_federal_in = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    payer_rtn = models.CharField(max_length=50, blank=True)
    fatca_filling = models.CharField(max_length=50, blank=True)
    state_in = models.CharField(max_length=50, blank=True)
    city_check = models.CharField(max_length=50, blank=True)
    payer_name = models.CharField(max_length=50, blank=True)
    tax_exempt_tax_credit = models.CharField(max_length=50, blank=True)
    recipient_last_name = models.CharField(max_length=50, blank=True)
    state_tax = models.CharField(max_length=50, blank=True)
    zip_code_check = models.CharField(max_length=50, blank=True)
    federal_income_tax = models.CharField(max_length=50, blank=True)
    recipient_first_name = models.CharField(max_length=50, blank=True)
    tax_exempt_interest = models.CharField(max_length=50, blank=True)
    state_recheck = models.CharField(max_length=50, blank=True)
    street_address = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=50, blank=True)
    interest_income = models.CharField(max_length=50, blank=True)
    early_withdrawal_penalty = models.CharField(max_length=50, blank=True)
    state_check = models.CharField(max_length=50, blank=True)
    interest_us_saving_bonds = models.CharField(max_length=50, blank=True)
    recipient_in = models.CharField(max_length=50, blank=True)
    market_discount = models.CharField(max_length=50, blank=True)
    investment_expenses = models.CharField(max_length=50, blank=True)
    foreign_country_us_possession = models.CharField(max_length=50, blank=True)
    account_number = models.CharField(max_length=50, blank=True)
    foreign_tax_paid = models.CharField(max_length=50, blank=True)


# 배당소득
class Ten99DIV(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    qualified_dividends = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)


# 정부 지원금, 실업수당 포함
class Ten99G(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    name = models.CharField(max_length=30, blank=True)

    city = models.CharField(max_length=30, blank=True)
    ssn = models.CharField(max_length=30, blank=True)


# 임금 소득 아닌 기타 소득
class Ten99MISC(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)


# 주택담보대출 이자 비용
class Ten99Mortgage(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)


# 학자금 대출 이자 비용
class Ten98EStudentLoanInterest(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)


# 학자금 비용 및 장학금
class Ten98TTuitionStatement(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)


# 13세 이하 자녀에게 들어간 유치원 및 탁아소 비용
class ChildCare(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
