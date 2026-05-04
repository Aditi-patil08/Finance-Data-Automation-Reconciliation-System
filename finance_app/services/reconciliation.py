from datetime import timedelta
from difflib import SequenceMatcher
from finance_app.models import BankStatement, InternalLedger, Ledger

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def auto_categorize(text):
    text = text.lower()
    if "swiggy" in text or "zomato" in text:
        return "Food"
    elif "uber" in text:
        return "Transport"
    elif "amazon" in text:
        return "Shopping"
    return "Others"

def run_reconciliation():
    bank_data = list(BankStatement.objects.all())
    ledger_data = list(InternalLedger.objects.all())

    matched = []
    unmatched_bank = []
    unmatched_ledger = ledger_data.copy()

    for b in bank_data:
        found = False
        for l in ledger_data:
            if (
                b.amount == l.amount and
                abs((b.date - l.date).days) <= 2 and
                similarity(b.narration, l.description) > 0.6
            ):
                matched.append((b, l))
                if l in unmatched_ledger:
                    unmatched_ledger.remove(l)
                found = True
                break
        if not found:
            unmatched_bank.append(b)

    Ledger.objects.all().delete()

    for b, l in matched:
        Ledger.objects.create(
            date=b.date,
            amount=b.amount,
            category=l.category or auto_categorize(b.narration),
            source="bank",
            reconciliation_status="matched"
        )

    for b in unmatched_bank:
        Ledger.objects.create(
            date=b.date,
            amount=b.amount,
            category=auto_categorize(b.narration),
            source="bank",
            reconciliation_status="unmatched"
        )

    for l in unmatched_ledger:
        Ledger.objects.create(
            date=l.date,
            amount=l.amount,
            category=l.category or "Others",
            source="internal",
            reconciliation_status="unmatched"
        )

    return {"matched": len(matched)}