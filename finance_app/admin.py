from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BankStatement, InternalLedger, Ledger

admin.site.register(BankStatement)
admin.site.register(InternalLedger)
admin.site.register(Ledger)