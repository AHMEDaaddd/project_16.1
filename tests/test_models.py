import pytest

from src.models import Category, LawnGrass, Product, Smartphone


def test_smartphone_attributes():
    phone = Smartphone("iPhone", "desc", 100000, 2, 95.5, "15", 512, "Gray")
    assert phone.name == "iPhone"
    assert phone.model == "15"
    assert phone.memory == 512
    assert phone.color == "Gray"


def test_lawngrass_attributes():
    grass = LawnGrass("Газон", "desc", 500, 5, "Россия", "7 дней", "Зелёный")
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зелёный"


def test_add_same_type_products():
    p1 = Smartphone("A", "desc", 1000, 1, 90, "X", 64, "Black")
    p2 = Smartphone("B", "desc", 2000, 2, 85, "Y", 128, "White")
    result = p1 + p2
    assert isinstance(result, Smartphone)
    assert result.price == 3000
    assert result.quantity == 3


def test_add_different_type_products():
    phone = Smartphone("A", "desc", 1000, 1, 90, "X", 64, "Black")
    grass = LawnGrass("Газон", "desc", 500, 1, "Россия", "7 дней", "Зелёный")
    with pytest.raises(TypeError):
        _ = phone + grass


def test_category_add_valid():
    phone = Smartphone("iPhone", "desc", 100000, 1, 95.5, "15", 512, "Gray")
    cat = Category("Смартфоны", "desc")
    cat.add_product(phone)
    assert phone in cat.products


def test_category_add_invalid():
    cat = Category("Смартфоны", "desc")
    with pytest.raises(TypeError):
        cat.add_product("непродукт")


def test_product_str():
    product = Product("Товар", "desc", 1500, 2)
    assert str(product) == "Товар, 1500 руб. (2 шт.)"
