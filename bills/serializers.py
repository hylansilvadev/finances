from rest_framework import serializers

from .models import Categories, Bills


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ["url", "id", "title"]


class BillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bills
        fields = [
            "url",
            "id",
            "status",
            "total_value",
            "issue_date",
            "due_date",
            "category",
            "created_at",
            "updated_at",
        ]
