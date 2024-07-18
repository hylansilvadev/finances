from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import AccountViewSet
from bills.views import BillsViewSet, CategoriesViewSet
from cards.views import BrandViewSet, CardViewSet
from transactions.views import (
    PaymentsViewSet,
    TransactionAccountToAccountViewSet,
    TransactionsViewSet,
)

router = DefaultRouter()
router.register(r"accounts", AccountViewSet)
router.register(r"categories", CategoriesViewSet)
router.register(r"bills", BillsViewSet)
router.register(r"brands", BrandViewSet)
router.register(r"cards", CardViewSet)
router.register(r"transactions", TransactionsViewSet)
router.register(r"transactions-account-to-account", TransactionAccountToAccountViewSet)
router.register(r"payments", PaymentsViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]