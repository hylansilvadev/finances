from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Transactions, TransactionAccountToAccount, Payments
from .serializers import (
    TransactionsSerializer,
    TransactionAccountToAccountSerializer,
    PaymentsSerializer,
)
from .utils import (
    get_account,
    get_amount,
    process_transaction,
    validate_request_data,
)


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def create(self, request, *args, **kwargs):
        try:
            validate_request_data(request.data, ["bill", "transaction_type"])
            account, card, bill, amount = process_transaction(request.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        try:
            validate_request_data(request.data, ["bill", "transaction_type"])
            account, card, bill, amount = process_transaction(request.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def handle_transaction(self, account, amount, transaction_type):
        if transaction_type == Transactions.TransactionType.DEPOSIT:
            account.deposit(amount)
        else:
            if not account.withdraw(amount):
                raise ValueError("Insufficient balance")

    def create(self, request, *args, **kwargs):
        if not all(
            key in request.data for key in ["account", "amount", "transaction_type"]
        ):
            return Response(
                {"error": "Account, amount, and transaction_type fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        account = get_account(request.data["account"])
        amount = get_amount(request.data["amount"])
        transaction_type = request.data["transaction_type"]

        try:
            self.handle_transaction(account, amount, transaction_type)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not all(
            key in request.data for key in ["account", "amount", "transaction_type"]
        ):
            return Response(
                {"error": "Account, amount, and transaction_type fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        account = get_account(request.data["account"])
        amount = get_amount(request.data["amount"])
        transaction_type = request.data["transaction_type"]

        try:
            self.handle_transaction(account, amount, transaction_type)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)


class TransactionAccountToAccountViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "delete"]
    queryset = TransactionAccountToAccount.objects.all()
    serializer_class = TransactionAccountToAccountSerializer

    def handle_transfer(self, from_account, to_account, amount):
        if not from_account.withdraw(amount):
            raise ValueError("Insufficient balance in the from_account")
        to_account.deposit(amount)
        to_account.save()

    def create(self, request, *args, **kwargs):
        if not all(
            key in request.data for key in ["from_account", "to_account", "amount"]
        ):
            return Response(
                {"error": "From_account, to_account, and amount fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        from_account = get_account(request.data["from_account"])
        to_account = get_account(request.data["to_account"])
        amount = get_amount(request.data["amount"])

        try:
            self.handle_transfer(from_account, to_account, amount)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
