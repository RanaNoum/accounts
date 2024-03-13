# student_rcd/serializers.py

# from rest_framework import serializers
# from .models import Customer, JournalEntry, Transaction

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'

# class JournalEntrySerializer(serializers.ModelSerializer):
#     customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
#     class Meta:
#         model = JournalEntry
#         fields = ['id', 'date', 'description', 'debit_account_id', 'debit_amount', 'credit_account_id', 'credit_amount', 'customer']

# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = '__all__'


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
    customer = CustomerSerializer(read_only=True)  # Nested serializer for customer details
    total_debit = serializers.SerializerMethodField()  # Custom field for total debit
    total_credit = serializers.SerializerMethodField()  # Custom field for total credit

    class Meta:
        model = Transaction
        fields = ['id', 'journal_entry', 'description', 'customer', 'total_debit', 'total_credit']

    def get_total_debit(self, obj):
        """
        Calculates the total debit amount for transactions associated with the journal entry of the current transaction.
        """
        journal_entry = obj.journal_entry
        total_debit = sum(transaction.amount for transaction in journal_entry.transactions.filter(amount__gt=0))
        return total_debit

    def get_total_credit(self, obj):
        """
        Calculates the total credit amount for transactions associated with the journal entry of the current transaction.
        """
        journal_entry = obj.journal_entry
        total_credit = sum(transaction.amount for transaction in journal_entry.transactions.filter(amount__lt=0))
        return total_credit
