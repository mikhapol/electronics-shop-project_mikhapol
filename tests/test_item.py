import pytest

from src.item import Item
from src.phone import Phone

"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.mark.parametrize('name, price, quantity, correct', [
    ("Телефон", 7000, 20, 140000),
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


def test_name():
    item = Item("Смартфон", 10000, 20)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    item = Item("Смартфон", 10000, 20)
    assert item.name == 'Смартфон'
    assert str(item) * 2 == 'СмартфонСмартфон'
    assert type(str(item)) == str


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


def test_instantiate_from_csv():
    Item.all.clear()
    Item.instantiate_from_csv()
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == '100'
    assert Item.all[0].quantity == '1'
