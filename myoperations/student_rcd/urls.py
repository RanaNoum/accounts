# # myapp/urls.py

# from django.urls import path
# from .views import CustomerListCreateView, JournalEntryListCreateView, TransactionListCreateView

# urlpatterns = [
#     path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
#     path('journal-entries/', JournalEntryListCreateView.as_view(), name='journal-entry-list-create'),
#     path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
# ]
# myapp/urls.py
# from .views import get_total_amounts
from django.urls import path
# from .views import get_all_debited_entries, get_all_credited_entries, get_all_customers_with_entries




from .views import (
    CustomerListCreateView, CustomerDetailView,
    JournalEntryListCreateView, JournalEntryDetailView,
    TransactionListCreateView, TransactionDetailView,
)

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    # path('customers/<int:customer_id>/journal_entries/',as_view(), name='create_journal_entry'),
    path('customers/<int:customer_id>/journal-entries/', JournalEntryListCreateView.as_view(), name='create-journal-entry'),
    
    path('journal-entries/', JournalEntryListCreateView.as_view(), name='journal-entry-list-create'),
    path('journal-entries/<int:pk>/', JournalEntryDetailView.as_view(), name='journal-entry-detail'),

    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),

    # path('allcustomers/', get_all_customers_with_entries, name='all-customers'),

    # path('get-total-amounts/', get_total_amounts, name='get_total_amounts'),
    # path('debited-entries/', get_all_debited_entries, name='debited-entries'),
    # path('credited-entries/', get_all_credited_entries, name='credited-entries'),

]
