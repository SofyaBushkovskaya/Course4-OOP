class Category:
    title: str
    description: str
    __products: list

    counted_categories = 0
    counted_product = 0

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.__products = products
        Category.counted_categories += 1
        Category.counted_product += len(self.__products)

    @classmethod
    def add_product(cls, product_list):
        cls.__products = product_list

    @property
    def product_list_enter(self):
        product = self.__products[0]
        return f"{self.title}, {product.price} руб. Остаток: {product.quantity} шт."

    def get_products(self):
        return self.__products


class Product:
    title: str
    description: str
    _price: int
    quantity: int

    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def creating_add_list(cls, product_list, title, description, price, quantity):
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
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректная.")
