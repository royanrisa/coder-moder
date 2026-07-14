# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: GardenMarket
def print_inventory_table(inventory):
    """Форматированный вывод таблицы остатков в консоль."""
    header = f"{'Товар':<20} {'Остаток':>10} {'Цена':>10} {'Сумма':>10}"
    print(header)
    print("-" * 50)
    for item, qty in inventory.items():
        line = f"{item:<20} {qty['quantity']:>10.0f} {qty['price']:>10.2f} {qty['sum']:>10.2f}"
        print(line)

def print_orders_table(orders):
    """Форматированный вывод таблицы заказов в консоль."""
    header = f"{'ID заказа':<8} {'Клиент':<20} {'Дата':<20} {'Сумма':>10}"
    print(header)
    print("-" * 56)
    for oid, order in orders.items():
        line = f"{oid:<8} {order['customer']:<20} {order['date']:<20} {order['total']:>10.2f}"
        print(line)

def print_customers_table(customers):
    """Форматированный вывод таблицы клиентов в консоль."""
    header = f"{'ID':<6} {'Имя':<30} {'Телефон':<14} {'Заказов':>8}"
    print(header)
    print("-" * 58)
    for cid, c in customers.items():
        line = f"{cid:<6} {c['name']:<30} {c['phone']:<14} {c['orders_count']:>8}"
        print(line)

def print_sales_plan(plan):
    """Форматированный вывод плана продаж в консоль."""
    header = f"{'Товар':<20} {'План':>10} {'Выполнено':>12} {'%':>6}"
    print(header)
    print("-" * 50)
    for item, sold in plan.items():
        pct = (sold['actual'] / sold['plan']) * 100 if sold['plan'] else 0
        line = f"{item:<20} {sold['plan']:>10.0f} {sold['actual']:>12.0f} {pct:>5.1f}%"
        print(line)

def format_number(n, width=10):
    """Оформление числа с пробелами для таблицы."""
    return f"{n:>{width}}"
