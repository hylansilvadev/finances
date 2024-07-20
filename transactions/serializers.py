# serializers.py
from rest_framework import serializers
from .models import Transactions, TransactionAccountToAccount, Payments


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    transaction_type_display = serializers.CharField(
        source="get_transaction_type_display", read_only=True
    )

    class Meta:
        model = Transactions
        fields = [
            "url",
            "id",
            "account",
            "amount",
            "transaction_type",
            "transaction_type_display",
            "timestamp",
        ]


class TransactionAccountToAccountSerializer(serializers.HyperlinkedModelSerializer):
    transaction_type_display = serializers.CharField(
        source="get_transaction_type_display", read_only=True
    )

    class Meta:
        model = TransactionAccountToAccount
        fields = [
            "url",
            "id",
            "from_account",
            "to_account",
            "amount",
            "transaction_type",
            "transaction_type_display",
            "timestamp",
        ]


class PaymentsSerializer(serializers.HyperlinkedModelSerializer):
    transaction_type_display = serializers.CharField(
        source="get_transaction_type_display", read_only=True
    )

    class Meta:
        model = Payments
        fields = [
            "url",
            "id",
            "account",
            "card",
            "bill",
            "transaction_type",
            "transaction_type_display",
        ]
