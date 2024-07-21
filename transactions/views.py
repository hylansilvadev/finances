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
    get_bill,
    get_card,
    validate_transaction,
)


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def create(self, request, *args, **kwargs):
        account = card = bill = None
        if "account" in request.data:
            account = get_account(request.data["account"])
        if "card" in request.data:
            card = get_card(request.data["card"])
        if "bill" in request.data:
            bill = get_bill(request.data["bill"])
        else:
            return Response(
                {"error": "Bill is required for this transaction"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        transaction_type = request.data["transaction_type"]
        is_valid, error_message = validate_transaction(
            account, card, bill, transaction_type
        )
        if not is_valid:
            return Response(
                {"error": error_message}, status=status.HTTP_400_BAD_REQUEST
            )

        if transaction_type == Payments.TransactionType.CREDIT:
            card.pay_with_credit(bill.total_value)
        elif transaction_type in [
            Payments.TransactionType.DEBIT,
            Payments.TransactionType.PIX,
            Payments.TransactionType.TED,
        ]:
            account.withdraw(bill.total_value)

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if "account" not in request.data:
            return Response(
                {"error": "Account field is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        account = get_account(request.data["account"])
        bill = None
        if "bill" in request.data:
            bill = get_bill(request.data["bill"])
            amount = bill.total_value if bill.total_value else 0
        else:
            amount = 0

        if account.balance < amount:
            return Response(
                {"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST
            )

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
