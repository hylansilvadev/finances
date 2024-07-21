import re
from uuid import UUID
from decimal import Decimal

from accounts.models import Account
from bills.models import Bills
from cards.models import Card
from .models import Payments

def extract_uuid(url):
    try:
        uuid_str = re.search(
            r"[\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}", url
        ).group(0)
        return UUID(uuid_str)
    except (AttributeError, ValueError):
        raise ValueError(f'O valor "{url}" não é um UUID válido')

def get_account(account_data):
    account_uuid = extract_uuid(account_data)
    return Account.objects.get(pk=account_uuid)


def get_card(card_data):
    card_uuid = extract_uuid(card_data)
    return Card.objects.get(pk=card_uuid)


def get_bill(bill_data):
    bill_uuid = extract_uuid(bill_data)
    return Bills.objects.get(pk=bill_uuid)


def validate_transaction(account, card, bill, transaction_type):
    amount = bill.total_value if bill.total_value else 0

    if transaction_type == Payments.TransactionType.CREDIT:
        if card.card_type != Card.CardType.BOTH or Card.CardType.CREDIT:
            return False, "This card is not credit card"
        if card.available_limit < amount:
            return False, "Insufficient credit card limit"

    if transaction_type in [
        Payments.TransactionType.DEBIT,
        Payments.TransactionType.PIX,
        Payments.TransactionType.TED,
    ]:
        if account.balance < amount:
            return False, "Insufficient account balance"

    return True, ""


def get_amount(amount_str):
    return Decimal(amount_str.replace(",", "."))
