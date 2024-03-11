
from django.urls import path
from .views import (
    CustomerListCreateView, CustomerDetailView,
    JournalEntryListCreateView, JournalEntryDetailView,
    TransactionListCreateView, TransactionDetailView,
    create_debit_entry, create_credit_entry,get_customer_data,delete_customer,
    delete_debit_entry,delete_credit_entry,create_transaction,
    delete_transaction,
)

urlpatterns = [
    path('create_customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers-list/', get_customer_data, name='get-customer-data'),
    
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<int:customer_id>/delete/', delete_customer, name='delete-customer'),

    path('journal-entries/', JournalEntryListCreateView.as_view(), name='journal-entry-list-create'),
    path('journal-entries/<int:pk>/', JournalEntryDetailView.as_view(), name='journal-entry-detail'),
    path('journal-entries/<int:journal_entry_id>/delete-debit/', delete_debit_entry, name='delete-debit-entry'),
    path('journal-entries/<int:journal_entry_id>/delete-credit/', delete_credit_entry, name='delete-credit-entry'),
   
    path('customers/<int:customer_id>/journal-entries/debit/', create_debit_entry, name='create-debit-entry'),

   
    path('customers/<int:customer_id>/journal-entries/credit/', create_credit_entry, name='create-credit-entry'),
    
    
    path('journal-entries/<int:journal_entry_id>/transactions/', create_transaction, name='create-transaction'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    
    path('transactions/<int:transaction_id>/delete/', delete_transaction, name='delete-transaction'),

    

]
