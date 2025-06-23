from typing import Optional

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. ({self.quantity} шт.)"

    def __add__(self, other: "Product") -> "Product":
        if type(self) != type(other):
            raise TypeError("Складывать можно только товары одного типа")
        return type(self)(
            self.name,
            self.description,
            self.price + other.price,
            self.quantity + other.quantity,
            *self._get_additional_attrs_add(other)
        )

    def _get_additional_attrs_add(self, other: object):
        return ()


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def _get_additional_attrs_add(self, other: object):
        return (self.efficiency, self.model, self.memory, self.color)


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def _get_additional_attrs_add(self, other: object):
        return (self.country, self.germination_period, self.color)


class Category:
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.product_count += len(self.products)

    def add_product(self, product: object) -> None:
        if not isinstance(product, Product):
            raise (
                TypeError("Можно добавлять только объекты Product или его наследников")
            )
        self.products.append(product)
        Category.product_count += 1
# 📌 Домашка 16.1 — SkyPro