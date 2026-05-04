from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import BankStatement, Ledger
from .services.reconciliation import run_reconciliation

@api_view(['GET'])
def run_recon(request):
    return Response(run_reconciliation())

@api_view(['GET'])
def summary(request):
    credits = BankStatement.objects.filter(type='credit').aggregate(Sum('amount'))['amount__sum'] or 0
    debits = BankStatement.objects.filter(type='debit').aggregate(Sum('amount'))['amount__sum'] or 0
    unmatched = Ledger.objects.filter(reconciliation_status='unmatched').aggregate(Sum('amount'))['amount__sum'] or 0

    return Response({
        "total_credits": credits,
        "total_debits": debits,
        "unmatched_amount": unmatched
    })

@api_view(['GET'])
def reconciliation_view(request):
    data = list(Ledger.objects.all().values())
    return Response(data)

@api_view(['GET'])
def category_breakdown(request):
    data = list(Ledger.objects.values('category').annotate(total=Sum('amount')))
    return Response(data)