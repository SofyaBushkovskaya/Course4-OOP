import pytest


class Category:
    title: str
    description: str
    products: list

    counted_categories = 0
    counted_product = 0

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products
        Category.counted_categories += 1
        Category.counted_product += len(self.products)


category1 = Category("Фрукты", "Свежие", ["Яблоко", "Банан", "Киви"])

print(category1.counted_categories, Category.counted_product)
print(category1.title)
print(category1.description)
print(category1.products)


class Product:
    title: str
    description: str
    price: int
    amounts: int

    def __init__(self, title, description, price, amounts):
        self.title = title
        self.description = description
        self.price = price
        self.amounts = amounts


product1 = Product("Фрукт", "Свежий", 15, 10)

print(product1.title)
print(product1.description)
print(product1.price)
print(product1.amounts)
