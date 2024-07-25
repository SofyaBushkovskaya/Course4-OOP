import json

from src.classes import Category, Product


def get_json_data(path_to_json):
    """Функция получения данных из JSON-файла"""
    try:
        with open(path_to_json, "r") as json_data_file:
            data = json.load(json_data_file)
            return data
    except FileNotFoundError:
        return []


def data_to_class_category(data):
    """Функция, которая читает JSON-файл и создаёт объекты класса Category"""
    categories = []
    for dict_ in data:
        products_list = []
        for i in range(len(dict_["products"])):
            products_list.append(dict_["products"][i]["title"])
        category = Category(dict_["title"], dict_["description"], products_list)
        category.display = (
            f"title - {category.title},"
            f"description - {category.description},"
            f"products: {category.products}"
        )
        categories.append(category.display)
    return categories


def data_to_class_product(data):
    """Функция. которая читает JSON-файл и создаёт объекты класса Product"""
    products = []
    for dict_ in data:
        for i in range(len(dict_["products"])):
            product = Product(
                dict["products"][i]["title"],
                dict["products"][i]["description"],
                dict["products"][i]["price"],
                dict["products"][i]["quantity"],
            )
            product.display = {
                f"title - {product.title}",
                f"description - {product.description}",
                f"price - {product.price}",
                f"amounts - {product.quantity}",
            }
            products.append(product.display)
    return products
