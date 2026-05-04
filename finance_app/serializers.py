from rest_framework import serializers
from .models import BankStatement, InternalLedger, Ledger

class BankStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStatement
        fields = '__all__'

class InternalLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalLedger
        fields = '__all__'

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'