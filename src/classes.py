from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый класс"""

    @abstractmethod
    def new_product(self, *args, **kwargs):
        """Абстрактный метод"""
        pass


class Mixin:
    """Класс Миксин"""

    def __init__(self, *args, **kwargs):
        """Инициализация класса миксин"""
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        """Вывод для разработчика"""
        return f"Создан объект класса {self.__class__.__name__}: {self}"


class Category:
    """Класс Категория"""

    title: str
    description: str
    __products: list

    counted_categories = 0
    counted_product = 0

    def __init__(self, title, description, products):
        """Метод для инициализации экземпляра класса."""
        self.title = title
        self.description = description
        self.__products = products
        Category.counted_categories += 1
        Category.counted_product += len(self.__products)

    @classmethod
    def add_product(cls, product):
        """Метод добавления продуктов."""
        cls.__products.append(product)

    @property
    def product_list_enter(self):
        """Метод вывода информации о продукте."""
        list_product = []
        for product in self.__products:
            result = (
                f"{self.title}, {product.price} руб. Остаток: {product.quantity} шт."
            )
            list_product.append(result)
        return list_product

    def get_products(self):
        """Метод для получения продукта."""
        return self.__products

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f"{self.title}, количество продуктов: {len(self.__products)} шт."


class Product(BaseProduct, Mixin):
    """Класс Продукт"""

    title: str
    description: str
    _price: int
    quantity: int

    def __init__(self, title, description, price, quantity, *args, **kwargs):
        """Метод для инициализации класса."""
        self.title = title
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__(*args, **kwargs)

    @classmethod
    def new_product(
        cls,
        products_list: list,
        title: str,
        description: str,
        price: float,
        quantity: int,
    ) -> Any:
        """Метод для создания товара и добавления его в список товаров с проверкой наличия дубликата."""
        for product in products_list:
            if product.title == title:
                if product._price < price:
                    product._price = price
                product.quantity += quantity
                return product

        # Проверяем, что объект является экземпляром класса Product или его наследником
        if (
            not isinstance(title, str)
            or not isinstance(description, str)
            or not isinstance(price, float)
            or not isinstance(quantity, int)
        ):
            raise TypeError("Неверный тип данных для создания продукта")

        new_product = cls(title, description, price, quantity)
        products_list.append(new_product)
        return products_list

    @property
    def price(self):
        """Геттер для атрибута цены."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для атрибута цены."""
        if new_price <= 0:
            print("Цена введена некорректная.")
        else:
            self._price = new_price
            print(self._price)
            print("Цена успешно изменена.")

    def __str__(self):
        return f"{self.title}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            raise TypeError("Можно складывать только одинаковые типы продуктов")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product, Mixin):

    performance: int
    model: str
    memory: int
    color: str

    def __init__(
        self, title, description, price, quantity, performance, model, memory, color
    ):
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(title, description, price, quantity)

    def new_product(self, *args, **kwargs):
        """Реализация метода new_product"""
        return super().new_product(*args, **kwargs)


class LawnGrass(Product, Mixin):

    country: str
    term: int
    color: str

    def __init__(self, title, description, price, quantity, country, term, color):
        self.country = country
        self.term = term
        self.color = color
        super().__init__(title, description, price, quantity)

    def new_product(self, *args, **kwargs):
        """Реализация метода new_product"""
        return super().new_product(*args, **kwargs)
