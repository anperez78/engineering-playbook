from decimal import Decimal
import pytest
from your_service.domain.value_objects import Money

def test_add_money_in_same_currency() -> None:
    result = Money(Decimal("10.25"), "EUR").add(Money(Decimal("2.75"), "EUR"))
    assert result == Money(Decimal("13.00"), "EUR")

def test_reject_addition_in_different_currencies() -> None:
    with pytest.raises(ValueError, match="different currencies"):
        Money(Decimal("10"), "EUR").add(Money(Decimal("2"), "USD"))
