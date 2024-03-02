# student_rcd/serializers.py

from rest_framework import serializers
from .models import Customer, JournalEntry, Transaction

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class JournalEntrySerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    class Meta:
        model = JournalEntry
        fields = ['id', 'date', 'description', 'debit_account_id', 'debit_amount', 'credit_account_id', 'credit_amount', 'customer']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
