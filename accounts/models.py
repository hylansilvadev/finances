import uuid
from django.db import models

from cards.models import Brand, Card

# Create your models here.


class Account(models.Model):
    class AccountType(models.TextChoices):
        SAVINGS = "SA", "Savings"
        CURRENT = "CR", "Current"
        SALARY = "SL", "Salary"
        BOTH = "BO", "Both"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank = models.ForeignKey(to=Brand, on_delete=models.SET_NULL, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, editable=False)
    card = models.ForeignKey(
        to=Card, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True
    )
    account_type = models.CharField(
        max_length=2,
        choices=AccountType,
        default=AccountType.CURRENT,
    )

    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return f"Account {self.bank} - {self.get_account_type_display()}"

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValueError("O saldo da conta não pode ser negativo.")
        super().save(*args, **kwargs)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        self.save()
