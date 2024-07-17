import uuid
from django.db import models

from cards.models import Brand, Card
from accounts.models import Account
# Create your models here.

class Bills(models.Model):
    
    OPEN = 'OP'
    PEDDING = 'PE'
    PAID = 'PA'
    LATE = 'LT'
    CANCELED = 'CL'
    
    ACCOUNT_TYPE_CHOICES = [
        (OPEN, 'Open'),
        (PEDDING, 'Pedding'),
        (PAID, 'Paid'),
        (LATE, 'Late')
        (CANCELED, 'Canceled')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=2,
        choices=ACCOUNT_TYPE_CHOICES,
        default=OPEN,
    )
    total_value = models.DecimalField(max_digits=10, decimal_places=2)