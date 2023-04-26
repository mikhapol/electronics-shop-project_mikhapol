import pytest

from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.mark.parametrize('name, price, quantity, correct', [
    ("Смартфон", 10000, 20, 200000),
    ("Ноутбук", 20000, 5, 100000)
])
def test_calculate_total_price(name, price, quantity, correct):
    item = Item(name, price, quantity)
    assert item.calculate_total_price() == correct


@pytest.mark.parametrize('name, price, quantity, correct', [
    ("Смартфон", 10000, 20, 5000),
    ("Ноутбук", 20000, 5, 10000)
])
def test_apply_discount(name, price, quantity, correct):
    item = Item(name, price, quantity)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == correct
