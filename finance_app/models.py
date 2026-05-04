# Create your models here.
from django.db import models

class BankStatement(models.Model):
    date = models.DateField()
    narration = models.CharField(max_length=255)
    amount = models.FloatField()
    type = models.CharField(max_length=10)

class InternalLedger(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.FloatField()
    category = models.CharField(max_length=100, null=True, blank=True)

class Ledger(models.Model):
    date = models.DateField()
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    source = models.CharField(max_length=20)
    reconciliation_status = models.CharField(max_length=20)
