# === Stage 20: Добавь восстановление записей из архива ===
# Project: GardenMarket
def restore_from_archive():
    """Восстанавливает записи из текстового архива (формат: 'id|name|qty' для товаров, 'client_id|order_id|date|total' для заказов)."""
    import os
    archive_path = "garden_market_archive.txt"
    if not os.path.exists(archive_path):
        print("Архив не найден.")
        return

    with open(archive_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    restored_products = 0
    restored_orders = 0

    for line in lines:
        parts = line.split("|")
        if len(parts) == 3 and parts[0].isdigit():
            pid, pname, pqty = int(parts[0]), parts[1], int(parts[2])
            product = Product(pid=pid, name=pname.strip(), quantity=pqty)
            products.append(product)
            restored_products += 1
        elif len(parts) == 4 and all(parts[i].isdigit() for i in range(3)):
            cid, oid, date_str, total = int(parts[0]), int(parts[1]), parts[2], float(parts[3])
            order = Order(id=oid, client_id=cid, date=date_str.strip(), total_cost=total)
            orders.append(order)
            restored_orders += 1

    print(f"Восстановлено: {restored_products} товаров и {restored_orders} заказов.")
