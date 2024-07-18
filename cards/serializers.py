from rest_framework import serializers

from .models import Card, Brand


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ["url", "id", "title"]


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = [
            "url",
            "id",
            "brand",
            "limit",
            "final_number",
            "due_day",
            "expire_date",
            "card_type",
            "created_at",
            "updated_at",
        ]
