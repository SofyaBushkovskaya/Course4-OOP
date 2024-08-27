from src.classes import Category, LawnGrass, Product, Smartphone

category1 = Category("Фрукты", "Свежие", ["Яблоко", "Банан", "Киви"])

print(category1.counted_categories, Category.counted_product)
print(category1.title)
print(category1.description)
print(category1.get_products())


product1 = Product("Фрукт", "Свежий", 15.0, 10)

print(product1.title)
print(product1.description)
print(product1.price)
print(product1.quantity)

product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)

# Устанавливаем новое значение цены с помощью сеттера
product1.price = 90.0

smartphone1 = Smartphone(
    "iPhone 12", "Смартфон фирмы Apple", 60000, 10, 4.5, "iPhone 12", 128, "Черный"
)
smartphone2 = Smartphone(
    "Samsung Galaxy S21",
    "Смартфон фирмы Samsung",
    50000,
    15,
    4.8,
    "Galaxy S21",
    256,
    "Белый",
)


lawn_grass1 = LawnGrass(
    "Газонная трава", "Трава для газона", 500, 10, "Россия", 14, "Зелёная"
)
