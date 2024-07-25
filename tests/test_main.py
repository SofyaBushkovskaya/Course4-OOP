import pytest

from src.main import Category, Product


@pytest.fixture
def category_1():
    category_1 = Category("Фрукты", "Свежие", ["Яблоко", "Банан", "Киви"])
    return category_1


def test_category_init(category_1):
    assert category_1.title == "Фрукты"
    assert category_1.description == "Свежие"
    assert category_1.products == ["Яблоко", "Банан", "Киви"]


@pytest.fixture
def product_1():
    product_1 = Product("Фрукт", "Свежий", 15, 10)
    return product_1


def test_product_init(product_1):
    assert product_1.title == "Фрукт"
    assert product_1.description == "Свежий"
    assert product_1.price == 15
    assert product_1.amounts == 10
