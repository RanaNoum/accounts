# from django.db import models

# Create your models here.
# myapp/models.py

# from django.db import models

# class Customer(models.Model):
#     name = models.CharField(max_length=255)
#     contact_information = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     customer_code = models.CharField(max_length=50, unique=True)

# class JournalEntry(models.Model):
#     date = models.DateField()
#     description = models.CharField(max_length=255)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

# class Transaction(models.Model):
#     journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
#     reference_id = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
# myapp/models.py

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_information = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    customer_code = models.CharField(max_length=50, unique=True)

class JournalEntry(models.Model): 
    date = models.DateField()
    description = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def update_entry(self, date, description, customer_id):
        self.date = date
        self.description = description
        self.customer_id = customer_id
        self.save()

class Transaction(models.Model):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    reference_id = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def update_transaction(self, reference_id, description, customer_id):
        self.reference_id = reference_id
        self.description = description
        self.customer_id = customer_id
        self.save()
