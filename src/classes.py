import unittest


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


class TestCategoryProductCount(unittest.TestCase):

    def setUp(self):
        # Сброс значений перед каждым тестом
        Category.counted_categories = 0
        Category.counted_product = 0

    def test_single_category_with_products(self):
        product1 = Product("Product 1", "Description 1", 100, 10)
        product2 = Product("Product 2", "Description 2", 200, 5)
        category = Category("Category 1", "Category Description", [product1, product2])

        self.assertEqual(Category.counted_categories, 1)
        self.assertEqual(Category.counted_product, 2)

    def test_multiple_categories(self):
        product1 = Product("Product 1", "Description 1", 100, 10)
        product2 = Product("Product 2", "Description 2", 200, 5)
        category1 = Category("Category 1", "Category Description", [product1])
        category2 = Category("Category 2", "Category Description", [product2])

        self.assertEqual(Category.counted_categories, 2)
        self.assertEqual(Category.counted_product, 2)

    def test_category_with_no_products(self):
        category = Category("Empty Category", "No products here", [])

        self.assertEqual(Category.counted_categories, 1)
        self.assertEqual(Category.counted_product, 0)


if __name__ == '__main__':
    unittest.main()