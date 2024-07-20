from rest_framework import viewsets, status
from rest_framework.response import Response
from decimal import Decimal

from bills.models import Bills
from .models import Transactions, TransactionAccountToAccount, Payments
from .serializers import (
    TransactionsSerializer,
    TransactionAccountToAccountSerializer,
    PaymentsSerializer,
)
from accounts.models import Account
import re
from uuid import UUID


def extract_uuid(url):
    try:
        uuid_str = re.search(
            r"[\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}", url
        ).group(0)
        return UUID(uuid_str)
    except (AttributeError, ValueError):
        raise ValueError(f'O valor "{url}" não é um UUID válido')


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def create(self, request, *args, **kwargs):
        if "account" not in request.data:
            return Response(
                {"error": "Account field is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        account_uuid = extract_uuid(request.data["account"])
        account = Account.objects.get(pk=account_uuid)

        if "bill" in request.data:
            bill = Bills.objects.get(pk=extract_uuid(request.data["bill"]))
            amount = bill.total_value if bill.total_value else 0
        else:
            amount = 0

        if account.balance < amount:
            return Response(
                {"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if "account" not in request.data:
            return Response(
                {"error": "Account field is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        account_uuid = extract_uuid(request.data["account"])
        account = Account.objects.get(pk=account_uuid)

        if "bill" in request.data:
            bill = Bills.objects.get(pk=extract_uuid(request.data["bill"]))
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

    def create(self, request, *args, **kwargs):
        if (
            "account" not in request.data
            or "amount" not in request.data
            or "transaction_type" not in request.data
        ):
            return Response(
                {"error": "Account, amount, and transaction_type fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        account_uuid = extract_uuid(request.data["account"])
        account = Account.objects.get(pk=account_uuid)
        amount = Decimal(request.data["amount"])
        transaction_type = request.data["transaction_type"]

        if transaction_type == Transactions.TransactionType.DEPOSIT:
            account.deposit(amount)
        else:
            if not account.withdraw(amount):
                return Response(
                    {"error": "Insufficient balance"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        response = super().create(request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):
        if (
            "account" not in request.data
            or "amount" not in request.data
            or "transaction_type" not in request.data
        ):
            return Response(
                {"error": "Account, amount, and transaction_type fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        account_uuid = extract_uuid(request.data["account"])
        account = Account.objects.get(pk=account_uuid)
        amount = Decimal(request.data["amount"])
        transaction_type = request.data["transaction_type"]

        if transaction_type == Transactions.TransactionType.DEPOSIT:
            account.deposit(amount)
        else:
            if not account.withdraw(amount):
                return Response(
                    {"error": "Insufficient balance"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        response = super().update(request, *args, **kwargs)
        return response


class TransactionAccountToAccountViewSet(viewsets.ModelViewSet):
    queryset = TransactionAccountToAccount.objects.all()
    serializer_class = TransactionAccountToAccountSerializer

    def create(self, request, *args, **kwargs):
        if (
            "from_account" not in request.data
            or "to_account" not in request.data
            or "amount" not in request.data
        ):
            return Response(
                {"error": "From_account, to_account, and amount fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        from_account_uuid = extract_uuid(request.data["from_account"])
        to_account_uuid = extract_uuid(request.data["to_account"])

        from_account = Account.objects.get(pk=from_account_uuid)
        to_account = Account.objects.get(pk=to_account_uuid)

        amount_str = request.data["amount"].replace(",", ".")
        amount = Decimal(amount_str)

        if not from_account.withdraw(amount):
            return Response(
                {"error": "Insufficient balance in the from_account"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        to_account.deposit(amount)
        to_account.save()  # Ensure to save the updated balance of the to_account

        response = super().create(request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):
        if (
            "from_account" not in request.data
            or "to_account" not in request.data
            or "amount" not in request.data
        ):
            return Response(
                {"error": "From_account, to_account, and amount fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        from_account_uuid = extract_uuid(request.data["from_account"])
        to_account_uuid = extract_uuid(request.data["to_account"])

        from_account = Account.objects.get(pk=from_account_uuid)
        to_account = Account.objects.get(pk=to_account_uuid)

        amount_str = request.data["amount"].replace(",", ".")
        amount = Decimal(amount_str)

        if not from_account.withdraw(amount):
            return Response(
                {"error": "Insufficient balance in the from_account"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        to_account.deposit(amount)
        to_account.save()  # Ensure to save the updated balance of the to_account

        response = super().update(request, *args, **kwargs)
        return response
