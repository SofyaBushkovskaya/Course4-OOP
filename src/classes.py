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
        for product in self.__products:
            return f"{self.title}, {product.price} руб. Остаток: {product.quantity} шт."

    def get_products(self):
        """Метод для получения продукта."""
        return self.__products

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f"{self.title}, количество продуктов: {len(self.__products)} шт."


class Product:
    """Класс Продукт"""

    title: str
    description: str
    _price: int
    quantity: int

    def __init__(self, title, description, price, quantity):
        """Метод для инициализации класса."""
        self.title = title
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def creating_add_list(cls, product_list, title, description, price, quantity):
        """Метод для создания товара и добавления его в список товаров с проверкой наличия дубликата."""
        for product in product_list:
            if product.title == title:
                if product._price < price:
                    product._price = price
                product.quantity += quantity
                return product
        new_product = cls(title, description, price, quantity)
        product_list.append(new_product)
        return product_list

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
        if type(self) != type(other):
            raise TypeError("Можно складывать только одинаковые типы продуктов")
        return self.price * self.quantity + other.price * other.quantity
