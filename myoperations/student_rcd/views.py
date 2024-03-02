from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.decorators import api_view
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


    @api_view(['POST'])
    def create_journal_entry(request, customer_id):
        if request.method == 'POST':
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                return Response({"error": f"Customer with ID {customer_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

            # Create the JournalEntry object
            journal_entry_data = {
                'date': request.data.get('date'),
                'description': request.data.get('description'),
                'debit_account_id': request.data.get('debit_account_id'),
                'debit_amount': request.data.get('debit_amount'),
                'credit_account_id': request.data.get('credit_account_id'),
                'credit_amount': request.data.get('credit_amount'),
                'customer': customer_id  # Pass the customer ID here
            }

            journal_entry_serializer = JournalEntrySerializer(data=journal_entry_data)

            if journal_entry_serializer.is_valid():
                journal_entry_serializer.save()
                return Response(journal_entry_serializer.data, status=status.HTTP_201_CREATED)
            return Response(journal_entry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
