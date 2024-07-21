from calendar import calendar
from datetime import date
from django.db import models
import uuid

# Create your models here.


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title


class Card(models.Model):
    class CardType(models.TextChoices):
        DEBIT = "DE", "Debit"
        CREDIT = "CR", "Credit"
        BENEFITS = "BF", "Both"
        BOTH = "BO", "Benefits"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.OneToOneField(
        to=Brand, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True
    )
    limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    available_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    final_number = models.IntegerField()
    due_day = models.PositiveSmallIntegerField()
    expire_date = models.DateField()
    card_type = models.CharField(
        max_length=2,
        choices=CardType,
        default=CardType.BOTH,
    )

    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return f"Card {self.final_number} - {(self.brand.title if self.brand else 'unbranded')} - {self.get_card_type_display()}"

    def next_due_date(self):
        today = date.today()
        current_month = today.month
        current_year = today.year

        if today.day > self.due_day:
            if current_month == 12:
                current_month = 1
                current_year += 1
            else:
                current_month += 1

        last_day_of_month = calendar.monthrange(current_year, current_month)[1]
        due_day = min(self.due_day, last_day_of_month)

        return date(current_year, current_month, due_day)

    def pay_with_credit(self, amount):
        if self.available_limit >= amount:
            self.available_limit -= amount
            self.save()
            return True
        return False
