from django.db import models
from taxpaas.settings import AUTH_USER_MODEL


class Mail(models.Model):
    sender = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='mail_sender_set'
    )
    recipient = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='mail_recipient_set'
    )
    headline = models.CharField(max_length=200)
    text = models.TextField()
    template = models.ForeignKey('communication.MailTemplate')
    created_date = models.DateTimeField(auto_now=True)


class MailTemplate(models.Model):
    category = models.CharField(max_length=100)
    text = models.TextField()
