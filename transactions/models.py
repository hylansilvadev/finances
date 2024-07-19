import uuid
from django.db import models
from accounts.models import Account
from bills.models import Bills
from cards.models import Card


class Transactions(models.Model):
    class TransactionType(models.TextChoices):
        WITHDRAW = "WD", "Withdraw"
        DEPOSIT = "DP", "Deposit"
        PIX = "PX", "PIX"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True, blank=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=2, choices=TransactionType, default=TransactionType.DEPOSIT
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.get_transaction_type_display()} - {self.amount} - {self.timestamp}"
        )


class TransactionAccountToAccount(models.Model):
    class TransactionType(models.TextChoices):
        DEPOSIT = "DP", "Deposit"
        TED = "TD", "TED"
        PIX = "PX", "PIX"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    from_account = models.ForeignKey(
        Account, related_name="transfers_out", on_delete=models.CASCADE
    )
    to_account = models.ForeignKey(
        Account, related_name="transfers_in", on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=2, choices=TransactionType, default=TransactionType.PIX
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transfer from {self.from_account} to {self.to_account} - {self.amount} - {self.timestamp}"


class Payments(models.Model):
    class TransactionType(models.TextChoices):
        MONEY = "MO", "Money"
        TED = "TD", "Ted"
        PIX = "PX", "Pix"
        CREDIT = "CD", "Credit"
        DEBIT = "DB", "Debit"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True, blank=True
    )
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)
    bill = models.ForeignKey(Bills, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(
        max_length=2, choices=TransactionType, default=TransactionType.MONEY
    )

    def __str__(self):
        return f"Payment of {(self.bill.category if self.bill.category else 'uncategorized')} - {(self.bill.total_value if self.bill.total_value else 'unvaluated')}"
