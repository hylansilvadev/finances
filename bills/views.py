from rest_framework import viewsets, generics

from bills.models import Bills, Categories
from bills.serializers import BillsSerializer, CategoriesSerializer


# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer


class PaidBillsListView(generics.ListAPIView):
    serializer_class = BillsSerializer

    def get_queryset(self):
        return Bills.objects.filter(status=Bills.BillStatus.PAID)
