from rest_framework import viewsets

from accounts.models import Account
from accounts.serializers import AccountSerializer


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
