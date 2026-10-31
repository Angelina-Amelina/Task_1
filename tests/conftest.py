import pytest
from unittest.mock import Mock
from burger import Burger
from database import Database
from data import BUN_NAME, BUN_PRICE, INGREDIENT_PRICE, INGREDIENT_TYPE, INGREDIENT_NAME

@pytest.fixture
def burger():
    return Burger()
@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun
@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE
    ingredient.get_name.return_value = INGREDIENT_NAME
    ingredient.get_price.return_value = INGREDIENT_PRICE
    return ingredient
@pytest.fixture
def full_burger(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger
@pytest.fixture
def db():
    return Database()