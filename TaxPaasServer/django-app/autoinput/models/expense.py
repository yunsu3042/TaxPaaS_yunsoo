from django.db import models

__all__ = ('Ten99INT', 'Ten99DIV', 'Ten99G', 'Ten99MISC', 'Ten99Mortgage',
           'Ten98EStudentLoanInterest', 'Ten98TTuitionStatement', 'ChildCare')


# 이자소득
class Ten99INT(models.Model):
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True, null=True)
    fields = models.CharField(max_length=30, blank=True)
    interest_income = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)


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
