# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: GardenMarket
def demo_run():
    print("=== Demo: GardenMarket ===")
    goods = [
        {"id": 1, "name": "Помидоры", "price": 80},
        {"id": 2, "name": "Морковь", "price": 45},
        {"id": 3, "name": "Свёкла", "price": 35},
    ]
    clients = [
        {"id": 1, "name": "Анна"},
        {"id": 2, "name": "Борис"},
    ]
    orders = []
    for i in range(10):
        g = goods[i % len(goods)]
        c = clients[i % len(clients)]
        qty = (i + 3) % 5
        total = g["price"] * qty
        order = {"id": i + 1, "client_id": c["id"], "goods": [g], "total": total}
        orders.append(order)
    print(f"Товары: {len(goods)}")
    print(f"Клиенты: {len(clients)}")
    print(f"Заказы: {len(orders)}")
    for o in orders[:3]:
        print(o)

demo_run()
