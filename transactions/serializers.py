# serializers.py
from rest_framework import serializers
from .models import Transactions, TransactionAccountToAccount, Payments


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    transaction_type_display = serializers.CharField(
        source="get_transaction_type_display", read_only=True
    )

    class Meta:
        model = Transactions
        fields = '__all__'


class TransactionAccountToAccountSerializer(serializers.HyperlinkedModelSerializer):
    transaction_type_display = serializers.CharField(
        source="get_transaction_type_display", read_only=True
    )

    class Meta:
        model = TransactionAccountToAccount
        fields = '__all__'


class PaymentsSerializer(serializers.HyperlinkedModelSerializer):
    transaction_type_display = serializers.CharField(
        source="get_transaction_type_display", read_only=True
    )

    class Meta:
        model = Payments
        fields = '__all__'
