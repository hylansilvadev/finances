from rest_framework import serializers

from .models import Transactions, TransactionAccountToAccount, Payments


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transactions
        fields = ["url", "id", "account", "amount", "transaction_type", "timestamp"]


class TransactionAccountToAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionAccountToAccount
        fields = [
            "url",
            "id",
            "from_account",
            "to_account",
            "amount",
            "transaction_type",
            "timestamp",
        ]


class PaymentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payments
        fields = ["url", "id", "account", "card", "bill", "transaction_type"]
