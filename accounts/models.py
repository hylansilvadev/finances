import uuid
from django.db import models

from cards.models import Brand, Card

# Create your models here.

class Account(models.Model):
    SAVINGS = 'SA'
    CURRENT = 'CR'
    SALARY = 'SL'
    BOTH = 'BO'
    
    ACCOUNT_TYPE_CHOICES = [
        (SAVINGS, 'Savings'),
        (CURRENT, 'Current'),
        (BOTH, 'Both'),
        (SALARY, 'Salary')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank = models.OneToOneField(to=Brand, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card = models.OneToOneField(to=Card, on_delete=models.SET_NULL, null=True, blank=True)
    account_type = models.CharField(
        max_length=2,
        choices=ACCOUNT_TYPE_CHOICES,
        default=CURRENT,
    )
    
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Account {self.bank} - {self.get_account_type_display()}"
