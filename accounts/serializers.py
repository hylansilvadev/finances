from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = [
            "url",
            "id",
            "bank",
            "amount",
            "card",
            "account_type",
            "created_at",
            "updated_at",
        ]
