from rest_framework import viewsets

from transactions.models import Payments, TransactionAccountToAccount, Transactions
from transactions.serializers import (
    PaymentsSerializer,
    TransactionAccountToAccountSerializer,
    TransactionsSerializer,
)


# Create your views here.
class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


class TransactionAccountToAccountViewSet(viewsets.ModelViewSet):
    queryset = TransactionAccountToAccount.objects.all()
    serializer_class = TransactionAccountToAccountSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
