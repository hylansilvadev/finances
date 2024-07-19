from rest_framework import viewsets
from .models import Transactions, TransactionAccountToAccount, Payments
from .serializers import (
    TransactionsSerializer,
    TransactionAccountToAccountSerializer,
    PaymentsSerializer,
)


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


class TransactionAccountToAccountViewSet(viewsets.ModelViewSet):
    queryset = TransactionAccountToAccount.objects.all()
    serializer_class = TransactionAccountToAccountSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
