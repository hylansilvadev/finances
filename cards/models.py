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
    DEBIT = 'DE'
    CREDIT = 'CR'
    BENEFITS = 'BF'
    BOTH = 'BO'
    
    CARD_TYPE_CHOICES = [
        (DEBIT, 'Debit'),
        (CREDIT, 'Credit'),
        (BOTH, 'Both'),
        (BENEFITS, 'Benefits')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.OneToOneField(to=Brand, on_delete=models.CASCADE)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    final_number = models.IntegerField()
    due_day = models.PositiveSmallIntegerField()
    expire_date = models.DateField()
    card_type = models.CharField(
        max_length=2,
        choices=CARD_TYPE_CHOICES,
        default=CREDIT,
    )

    def __str__(self):
        return f"Card {self.final_number} - {self.brand.title} - {self.get_card_type_display()}"
    
    def next_due_date(self):
        today = date.today()
        current_month = today.month
        current_year = today.year

        # If today's date is past the due day this month, set the due date to next month
        if today.day > self.due_day:
            if current_month == 12:
                current_month = 1
                current_year += 1
            else:
                current_month += 1

        # Handle months with fewer days than the due_day (e.g., February)
        last_day_of_month = calendar.monthrange(current_year, current_month)[1]
        if self.due_day > last_day_of_month:
            due_day = last_day_of_month
        else:
            due_day = self.due_day

        return date(current_year, current_month, due_day)