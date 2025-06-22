# 📱🌱 OOP Inheritance Project

Домашнее задание 16.1 (SkyPro)

## 📦 Реализованная функциональность

В рамках проекта выполнены следующие задачи:

### ✅ Классы:
- `Product` — базовый класс товара
- `Smartphone(Product)` — смартфоны с доп. атрибутами: `efficiency`, `model`, `memory`, `color`
- `LawnGrass(Product)` — газонная трава с доп. атрибутами: `country`, `germination_period`, `color`
- `Category` — хранит список продуктов и общий счётчик продуктов

### ✅ Ограничения:
- Сложение (`__add__`) — только объекты одного типа (иначе `TypeError`)
- Метод `add_product()` — добавляет только объекты `Product` или его наследников (иначе `TypeError`)

### ✅ Тесты:
- Используется `pytest`
- Все ключевые классы и методы протестированы
- Покрытие тестами >75%

## 🚀 Как запустить

1. Установка зависимостей:
```bash
poetry install
```

2. Запуск тестов с покрытием:
```bash
poetry run pytest --cov=src --cov-report=term-missing
```

## 🧪 Примеры
```python
smartphone1 + smartphone2  # работает
smartphone1 + grass1       # вызывает TypeError

cat = Category("Смартфоны", "...")
cat.add_product(smartphone1)  # работает
cat.add_product("строка")     # вызывает TypeError
```

## 📁 Структура проекта
```
src/
├── models.py     # Классы: Product, Smartphone, LawnGrass, Category
├── main.py       # Пример запуска

tests/
├── test_models.py

README.md
pyproject.toml
```

> ✅ Готово к сдаче наставнику: вся логика реализована, работает без ошибок, покрытие тестами есть.
