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


    

@api_view(['GET'])
def get_customer_data(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customer_data = []
        for customer in customers:
            customer_dict = {}
            customer_dict['customer'] = CustomerSerializer(customer).data
            customer_dict['transactions'] = []
            total_debit = 0
            total_credit = 0
            journal_entries = JournalEntry.objects.filter(customer=customer)
            for entry in journal_entries:
                debit_entries = Transaction.objects.filter(journal_entry=entry, description__icontains='debit')
                credit_entries = Transaction.objects.filter(journal_entry=entry, description__icontains='credit')
                transaction_data = {
                    'journal_entry': JournalEntrySerializer(entry).data,
                    'debit_entries': TransactionSerializer(debit_entries, many=True).data,
                    'credit_entries': TransactionSerializer(credit_entries, many=True).data,
                }
                total_debit += sum(entry.debit_amount for entry in debit_entries)
                total_credit += sum(entry.credit_amount for entry in credit_entries)
                customer_dict['transactions'].append(transaction_data)
            customer_dict['total_debit'] = total_debit
            customer_dict['total_credit'] = total_credit
            customer_data.append(customer_dict)
        return Response(customer_data)






@api_view(['DELETE'])
def delete_debit_entry(request, journal_entry_id):
  """
  Deletes a debit journal entry permanently from the database.

  Args:
      request: The incoming Django request object.
      journal_entry_id: The ID of the journal entry to be deleted.

  Returns:
      A Django response object with appropriate status code and message.
  """
  if request.method == 'DELETE':
    try:
      journal_entry = JournalEntry.objects.get(pk=journal_entry_id)
      # Check if it's a debit entry
      if journal_entry.debit_amount > 0:
        journal_entry.delete()
        return Response({"message": "Debit entry deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
      else:
        return Response({"error": "This is not a debit entry"}, status=status.HTTP_400_BAD_REQUEST)
    except JournalEntry.DoesNotExist:
      return Response({"error": "Journal entry not found"}, status=status.HTTP_404_NOT_FOUND)
  else:
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_credit_entry(request, journal_entry_id):
  """
  Deletes a credit journal entry permanently from the database.

  Args:
      request: The incoming Django request object.
      journal_entry_id: The ID of the journal entry to be deleted.

  Returns:
      A Django response object with appropriate status code and message.
  """
  if request.method == 'DELETE':
    try:
      journal_entry = JournalEntry.objects.get(pk=journal_entry_id)
      # Check if it's a credit entry
      if journal_entry.credit_amount > 0:
        journal_entry.delete()
        return Response({"message": "Credit entry deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
      else:
        return Response({"error": "This is not a credit entry"}, status=status.HTTP_400_BAD_REQUEST)
    except JournalEntry.DoesNotExist:
      return Response({"error": "Journal entry not found"}, status=status.HTTP_404_NOT_FOUND)
  else:
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_customer(request, customer_id):
  """
  Deletes a customer permanently from the database.

  Args:
      request: The incoming Django request object.
      customer_id: The ID of the customer to be deleted.

  Returns:
      A Django response object with appropriate status code and message.
  """
  if request.method == 'DELETE':
    try:
      customer = Customer.objects.get(pk=customer_id)
      customer.delete()
      return Response({"message": "Customer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Customer.DoesNotExist:
      return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)
  else:
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST'])
def create_debit_entry(request, customer_id):
    if request.method == 'POST':
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({"error": f"Customer with ID {customer_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Deserialize the request data
        date = request.data.get('date')
        description = request.data.get('description')
        debit_account_id = request.data.get('debit_account_id')
        debit_amount = request.data.get('debit_amount')

        # Create the debit journal entry
        debit_journal_entry_data = {
            'date': date,
            'description': description,
            'debit_account_id': debit_account_id,
            'debit_amount': debit_amount,
            'customer': customer_id
        }

        # Serialize the data and save the journal entry
        debit_serializer = JournalEntrySerializer(data=debit_journal_entry_data)

        if debit_serializer.is_valid():
            debit_serializer.save()
            return Response({"message": "Debit entry created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(debit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_credit_entry(request, customer_id):
    if request.method == 'POST':
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({"error": f"Customer with ID {customer_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Deserialize the request data
        date = request.data.get('date')
        description = request.data.get('description')
        credit_account_id = request.data.get('credit_account_id')
        credit_amount = request.data.get('credit_amount')

        # Create the credit journal entry
        credit_journal_entry_data = {
            'date': date,
            'description': description,
            'credit_account_id': credit_account_id,
            'credit_amount': credit_amount,
            'customer': customer_id
        }

        # Serialize the data and save the journal entry
        credit_serializer = JournalEntrySerializer(data=credit_journal_entry_data)

        if credit_serializer.is_valid():
            credit_serializer.save()
            return Response({"message": "Credit entry created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(credit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer




@api_view(['POST'])
def create_transaction(request, journal_entry_id):
  """
  Creates a new transaction associated with a specific journal entry.

  Args:
      request: The incoming Django request object.
      journal_entry_id: The ID of the journal entry to associate the transaction with.

  Returns:
      A Django response object with appropriate status code and message.
  """
  if request.method == 'POST':
    try:
      journal_entry = JournalEntry.objects.get(pk=journal_entry_id)
    except JournalEntry.DoesNotExist:
      return Response({"error": "Journal entry not found"}, status=status.HTTP_404_NOT_FOUND)

    # Deserialize the request data
    account_id = request.data.get('account_id')
    amount = request.data.get('amount')
    description = request.data.get('description', '')  # Set default empty description

    # Create the transaction
    transaction_data = {
      'journal_entry': journal_entry,
      'account_id': account_id,
      'amount': amount,
      'description': description,
    }

    serializer = TransactionSerializer(data=transaction_data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message": "Transaction created successfully"}, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  else:
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_transaction(request, transaction_id):
  """
  Deletes a transaction permanently from the database.

  Args:
      request: The incoming Django request object.
      transaction_id: The ID of the transaction to be deleted.

  Returns:
      A Django response object with appropriate status code and message.
  """
  if request.method == 'DELETE':
    try:
      transaction = Transaction.objects.get(pk=transaction_id)
      transaction.delete()
      return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Transaction.DoesNotExist:
      return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
  else:
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)