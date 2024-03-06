
from django.urls import path
from .views import (
    CustomerListCreateView, CustomerDetailView,
    JournalEntryListCreateView, JournalEntryDetailView,
    TransactionListCreateView, TransactionDetailView,
    create_debit_entry, create_credit_entry,get_customer_data,
)

urlpatterns = [
    path('customers-list/', get_customer_data, name='get-customer-data'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

   
    path('customers/<int:customer_id>/journal-entries/debit/', create_debit_entry, name='create-debit-entry'),

   
    path('customers/<int:customer_id>/journal-entries/credit/', create_credit_entry, name='create-credit-entry'),
    path('journal-entries/', JournalEntryListCreateView.as_view(), name='journal-entry-list-create'),
    path('journal-entries/<int:pk>/', JournalEntryDetailView.as_view(), name='journal-entry-detail'),

    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),

    

]
