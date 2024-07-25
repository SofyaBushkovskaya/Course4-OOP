from typing import Any

import pytest
from src.classes import Category, Product


@pytest.fixture
def product1() -> Any:
    return Product("топ", "для занятия спортом", 599, 10)


@pytest.fixture
def product2() -> Any:
    return Product("топ2", "для занятия спортом2", 599, 10)


@pytest.fixture
def category_object(product1: Any, product2: Any) -> Any:
    """Тест получает на вход класс Category для удобства дальнейшей работы"""
    return Category("одежда", "для спорта", [product1, product2])


def test_init_category(category_object: Any, product1: Any, product2: Any) -> None:
    """
    Тест проверяет корректность инициализации объектов класса Category.
    Также тест считает количество продуктов и категорий.
    """
    assert category_object.title == "одежда"
    assert category_object.description == "для спорта"
    assert category_object._Category__products == [product1, product2]
    assert category_object.counted_categories == 1
    assert category_object.counted_product == 2


@pytest.fixture
def product_3():
    product_3 = Product("Фрукт", "Свежий", 15, 10)
    return product_3


def test_product_init(product_3):
    assert product_3.title == "Фрукт"
    assert product_3.description == "Свежий"
    assert product_3.price == 15
    assert product_3.quantity == 10


@pytest.fixture
def sample_category() -> Any:
    return Category("Electronics", "Category for electronic devices", [])


@pytest.fixture
def sample_product_list() -> list:
    return [Product("Laptop", "Powerful laptop", 1500, 10), Product("Phone", "Smartphone", 800, 20)]


def test_category_initialization(sample_category: Any) -> None:
    assert sample_category.title == "Electronics"
    assert sample_category.description == "Category for electronic devices"
    assert sample_category.counted_categories == 2


def test_product_initialization(sample_product_list: list) -> None:
    assert len(sample_product_list) == 2
    assert sample_product_list[0].title == "Laptop"
    assert sample_product_list[1].quantity == 20
    assert Category.counted_product == 2


def test_product_creation(sample_product_list: list) -> None:
    new_product = Product.creating_add_list(sample_product_list, "Laptop", "New powerful laptop", 1700, 5)
    assert new_product.quantity == 15
    assert len(sample_product_list) == 2


def test_category_init() -> None:
    category = Category("Electronics", "Electronic devices", [])
    assert category.title == "Electronics"
    assert category.description == "Electronic devices"
    assert category.get_products() == []


# Тестирование класса Product
def test_product_init_2() -> None:
    product = Product("Laptop", "Powerful laptop", 1000, 5)
    assert product.title == "Laptop"
    assert product.description == "Powerful laptop"
    assert product._price == 1000
    assert product.quantity == 5


def test_price_getter() -> None:
    product = Product("товар", "описание", 100, 10)
    assert product.price == 100


def test_price_setter() -> None:
    product = Product("товар", "описание", 100, 10)
    product._price = 90
    assert product.price == 90


def test_price_setter_negative() -> None:
    product = Product("товар", "описание", 100, 10)
    product.price = -10
    assert product.price == 100
