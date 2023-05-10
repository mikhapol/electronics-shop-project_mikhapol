import pytest

from src.items import Item
from src.phone import Phone


def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 11", 100_000, 10, 1)
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Телефон", 5000, 15)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item2 + phone1 == 20
    assert phone1 + phone2 == 15
    with pytest.raises(ValueError):
        phone1 + 15000
    with pytest.raises(ValueError):
        item1 + 15000


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
