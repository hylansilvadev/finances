from rest_framework import serializers

from .models import Categories, Bills


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class BillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'

