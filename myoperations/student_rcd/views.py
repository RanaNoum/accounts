# from django.shortcuts import render

# # Create your views here.
# # myapp/views.py

# from rest_framework import generics
# from .models import Customer, JournalEntry, Transaction
# from .serializers import CustomerSerializer, JournalEntrySerializer, TransactionSerializer

# class CustomerListCreateView(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class JournalEntryListCreateView(generics.ListCreateAPIView):
#     queryset = JournalEntry.objects.all()
#     serializer_class = JournalEntrySerializer

# class TransactionListCreateView(generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
# myapp/views.py

from rest_framework import generics
from .models import Customer, JournalEntry, Transaction
from .serializers import CustomerSerializer, JournalEntrySerializer, TransactionSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class JournalEntryListCreateView(generics.ListCreateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
from django.db import connection
from django.http import JsonResponse

def get_total_amounts(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT 
                SUM(debit_amount) AS total_debit_amount
            FROM 
                journal_entries
            WHERE 
                debit_amount > 0;
            """
        )
        total_debit_amount = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT 
                SUM(credit_amount) AS total_credit_amount
            FROM 
                journal_entries
            WHERE 
                credit_amount > 0;
            """
        )
        total_credit_amount = cursor.fetchone()[0]

    return JsonResponse({
        'total_debit_amount': total_debit_amount,
        'total_credit_amount': total_credit_amount
    })
