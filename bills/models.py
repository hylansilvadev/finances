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
    OPEN = "OP"
    PEDDING = "PE"
    PAID = "PA"
    LATE = "LT"
    CANCELED = "CL"

    BILL_TYPE_CHOICES = [
        (OPEN, "Open"),
        (PEDDING, "Pedding"),
        (PAID, "Paid"),
        (LATE, "Late"),
        (CANCELED, "Canceled"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=2,
        choices=BILL_TYPE_CHOICES,
        default=OPEN,
    )
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField()
    due_date = models.DateField()

    category = models.OneToOneField(
        Categories, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateField(default=datetime.now, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return f"Bill: {self.category} - value: {self.total_value}"