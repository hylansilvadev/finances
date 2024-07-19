from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    bank_name = serializers.SerializerMethodField()
    account_type_display = serializers.CharField(
        source="get_account_type_display", read_only=True
    )

    class Meta:
        model = Account
        fields = [
            "url",
            "id",
            "bank",
            "bank_name",
            "amount",
            "card",
            "account_type",
            "account_type_display",
            "created_at",
            "updated_at",
        ]

    def get_bank_name(self, obj):
        return obj.bank.title if obj.bank else None
