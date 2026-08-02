# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: GardenMarket
def check_and_repair_data():
    """Проверка целостности данных и простой ремонт проблем."""
    issues = []
    
    # Проверка: все товары имеют положительные цены
    for i, item in enumerate(items):
        if item['price'] <= 0:
            items[i]['price'] = default_prices.get(item['name'], 10)
            issues.append(f"Исправлена цена товара '{item['name']}'")
    
    # Проверка: все заказанные количества не превышают доступное количество
    for i, order in enumerate(orders):
        if 'items' not in order:
            continue
        for j, item_order in enumerate(order['items']):
            product_name = item_order.get('product', '')
            quantity_ordered = item_order.get('quantity', 0)
            
            # Найти товар в products по имени
            product = None
            for k, p in enumerate(products):
                if p['name'] == product_name:
                    product = p
                    break
            
            if product and quantity_ordered > product['stock']:
                order['items'][j]['quantity'] = product['stock']
                issues.append(f"Ограничено количество заказа '{order.get('id', 'unknown')}'")
    
    # Проверка: все клиенты имеют valid email (простая форма)
    for i, client in enumerate(clients):
        if not client.get('email'):
            clients[i]['email'] = f"client_{i+1}@example.com"
            issues.append(f"Установлен дефолтный email для клиента {i+1}")
    
    return issues
