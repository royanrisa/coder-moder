# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: GardenMarket
def generate_summary():
    print("=== СВОДКА GARDENMARKET ===")
    if not products:
        print("Товары отсутствуют.")
    else:
        total_value = sum(p['price'] * p['stock'] for p in products)
        low_stock = [p for p in products if p['stock'] < 5]
        print(f"Всего товаров: {len(products)}")
        print(f"Общая стоимость остатков: {total_value:.2f} руб.")
        if low_stock:
            print(f"Товары с низким запасом (<5 шт): {[p['name'] for p in low_stock]}")
    if not orders:
        print("Заказы отсутствуют.")
    else:
        total_revenue = sum(o['total_price'] for o in orders)
        avg_order_value = total_revenue / len(orders) if orders else 0
        print(f"Всего заказов: {len(orders)}")
        print(f"Общий доход: {total_revenue:.2f} руб.")
        print(f"Средний чек: {avg_order_value:.2f} руб.")
    if not clients:
        print("Клиенты отсутствуют.")
    else:
        active_clients = len(set(c['id'] for c in clients))
        print(f"Всего клиентов: {active_clients}")
