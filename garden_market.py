# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: GardenMarket
import json
from datetime import date, timedelta

# --- Базовая структура и демонстрационные данные для GardenMarket ---

class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "stock": self.stock}

class Order:
    def __init__(self, id, customer_id, items, total_price):
        self.id = id
        self.customer_id = customer_id
        self.items = items  # список словарей {product_id: quantity}
        self.total_price = total_price
        self.date = date.today()

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "items": self.items,
            "total_price": self.total_price,
            "date": self.date.isoformat()
        }

class Customer:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {"id": self.id, "name": self.name, "phone": self.phone}

# --- Демонстрационные данные ---

products_db = [
    Product(1, "Варенье из смородины", 450.0, 20),
    Product(2, "Моченая капуста", 300.0, 15),
    Product(3, "Квашеная капуста", 250.0, 30),
    Product(4, "Пикантные огурцы", 500.0, 10),
]

customers_db = [
    Customer(1, "Иванов Иван", "+79001112233"),
    Customer(2, "Петрова Анна", "+79004445566"),
]

orders_db = [
    Order(1, 1, {1: 2}, 900.0),
    Order(2, 2, {3: 5}, 1250.0),
]

# --- Точка входа и функция запуска демо ---

def run_demo():
    print("=== GardenMarket Demo ===")
    print(f"Товаров: {len(products_db)}")
    print(f"Клиентов: {len(customers_db)}")
    print(f"Заказов: {len(orders_db)}")
    
    # Пример вывода остатков
    for p in products_db:
        print(f"  - {p.name}: {p.stock} шт. ({p.price} руб.)")

if __name__ == "__main__":
    run_demo()
