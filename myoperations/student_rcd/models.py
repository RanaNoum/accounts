
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_information = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    customer_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class JournalEntry(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    debit_account_id = models.IntegerField(null=True, blank=True)
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    credit_account_id = models.IntegerField(null=True, blank=True)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.description}"

class Transaction(models.Model):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    reference_id = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.reference_id} - {self.description}"
