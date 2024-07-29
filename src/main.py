from src.classes import Category, Product

category1 = Category("Фрукты", "Свежие", ["Яблоко", "Банан", "Киви"])

print(category1.counted_categories, Category.counted_product)
print(category1.title)
print(category1.description)
print(category1.get_products())


product1 = Product("Фрукт", "Свежий", 15, 10)

print(product1.title)
print(product1.description)
print(product1.price)
print(product1.quantity)

product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)

# Устанавливаем новое значение цены с помощью сеттера
product1.price = 90.0
