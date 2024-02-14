# # myapp/urls.py

# from django.urls import path
# from .views import CustomerListCreateView, JournalEntryListCreateView, TransactionListCreateView

# urlpatterns = [
#     path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
#     path('journal-entries/', JournalEntryListCreateView.as_view(), name='journal-entry-list-create'),
#     path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
# ]
# myapp/urls.py

from django.urls import path
from .views import (
    CustomerListCreateView, CustomerDetailView,
    JournalEntryListCreateView, JournalEntryDetailView,
    TransactionListCreateView, TransactionDetailView,
)

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    
    path('journal-entries/', JournalEntryListCreateView.as_view(), name='journal-entry-list-create'),
    path('journal-entries/<int:pk>/', JournalEntryDetailView.as_view(), name='journal-entry-detail'),

    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
]
