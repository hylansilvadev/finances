from rest_framework import viewsets

from cards.models import Brand, Card
from cards.serializers import BrandSerializer, CardSerializer


# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer