from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from bills.models import Bills
from transactions.models import Payments


@receiver(post_save, sender=Payments)
def process_payment(sender, instance, created, **kwargs):
    if created:
        account = instance.account
        amount = instance.bill.total_value
        bill = instance.bill  # Ajuste: instance.bill ao invés de instance.bills
        if account:
            success = account.withdraw(amount)
            
            if not success:
                instance.delete()
                raise ValueError("Saldo insuficiente na conta para efetuar o pagamento.")
            else:
                bill.paid_bill()
