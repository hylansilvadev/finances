import uuid
from django.utils.timezone import now
from datetime import datetime
from django.db import models

# Create your models here.

class Bills(models.Model):
    
    OPEN = 'OP'
    PEDDING = 'PE'
    PAID = 'PA'
    LATE = 'LT'
    CANCELED = 'CL'
    
    CREDIT_CARD = 'CC'
    DEBIT_CARD = 'DC'
    MONEY = 'MO'
    
    BILL_TYPE_CHOICES = [
        (OPEN, 'Open'),
        (PEDDING, 'Pedding'),
        (PAID, 'Paid'),
        (LATE, 'Late'),
        (CANCELED, 'Canceled'),
    ]
    
    PAYMENT_TYPE_CHOICES = [
        (CREDIT_CARD, 'Credit Card'),
        (DEBIT_CARD, 'Debit Card'),
        (MONEY, 'Money'),
    ]
    
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=2,
        choices=BILL_TYPE_CHOICES,
        default=OPEN,
    )
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField(default=datetime.now())
    due_date = models.DateField(default=datetime.now())
    payment_type = models.CharField(
        max_length=2,
        choices=PAYMENT_TYPE_CHOICES,
        default=MONEY,
    )
    created_at = models.DateField(auto_now=True, editable=False)
    updated_at = models.DateField(auto_now=True)
    