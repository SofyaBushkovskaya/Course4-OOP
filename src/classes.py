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