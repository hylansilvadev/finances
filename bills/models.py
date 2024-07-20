import uuid
from datetime import datetime
from django.db import models

# Create your models here.


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title


class Bills(models.Model):
    class BillStatus(models.TextChoices):
        OPEN = "OP", "Open"
        PENDING = "PE", "Pending"
        PAID = "PA", "Paid"
        LATE = "LT", "Late"
        CANCELED = "CL", "Canceled"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=2,
        choices=BillStatus,
        default=BillStatus.OPEN,
    )
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField()
    due_date = models.DateField()

    category = models.OneToOneField(
        Categories, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return f"Bill: {(self.category if self.category else 'uncategorized')} - value: {self.total_value}"
    
    def paid_bill(self):
        self.status = self.BillStatus.PAID
        self.save()