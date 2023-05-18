import pytest, sys

from src.items import Item, InstantiateCSVError, FILE_ITEMS
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


def test_instantiate_from_csv():
    # Item.all.clear()
    item = Item("Смартфон", 10000, 20)
    Item.instantiate_from_csv()
    assert item.name == 'Смартфон'
    assert item.price == 10000
    assert item.quantity == 20

    # with pytest.raises(InstantiateCSVError):
    #     Item.instantiate_from_csv()

    # Item.instantiate_from_csv()
    # captured = capsys.readouterr()
    # assert captured.out == "Файл item.csv поврежден\n"

