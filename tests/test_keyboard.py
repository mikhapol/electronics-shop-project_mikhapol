import pytest

from src.keyboard import Keyboard


# assert str(kb) == "Dark Project KD87A"
def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"


def test_property():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    assert str(kb.language) == "EN"
    with pytest.raises(AttributeError):
        kb.language = 'CH'
