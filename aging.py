#!/usr/bin/env python3
"""Invoice aging analyzer."""
from datetime import datetime, timedelta

def analyze_invoices(invoices):
    today = datetime.now()
    buckets = {"0-30": 0, "31-60": 0, "61-90": 0, "90+": 0}
    for inv in invoices:
        days = (today - inv["date"]).days
        amount = inv["amount"]
        if days <= 30:
            buckets["0-30"] += amount
        elif days <= 60:
            buckets["31-60"] += amount
        elif days <= 90:
            buckets["61-90"] += amount
        else:
            buckets["90+"] += amount
    return buckets

if __name__ == "__main__":
    sample = [
        {"date": datetime.now() - timedelta(days=10), "amount": 25000},
        {"date": datetime.now() - timedelta(days=45), "amount": 40000},
        {"date": datetime.now() - timedelta(days=100), "amount": 15000},
    ]
    print(analyze_invoices(sample))
