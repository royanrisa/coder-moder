# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: GardenMarket
def show_menu():
    print("\n=== Меню GardenMarket ===")
    print("1. Показать товары")
    print("2. Добавить товар")
    print("3. Создать заказ")
    print("4. Просмотреть клиентов")
    print("5. Выход")
    choice = input("Выберите действие (1-5): ")
    return choice

def handle_choice(choice, products, orders, clients):
    if choice == '1':
        for i, p in enumerate(products, 1):
            print(f"{i}. {p['name']} - {p['price']} руб. (Остаток: {p['stock']})")
    elif choice == '2':
        name = input("Название товара: ")
        price = float(input("Цена: "))
        stock = int(input("Количество на складе: "))
        products.append({'name': name, 'price': price, 'stock': stock})
        print(f"Товар '{name}' добавлен.")
    elif choice == '3':
        if not clients:
            print("Нет клиентов. Сначала добавьте клиента (выберите 4).")
            return
        client_name = input("Имя клиента: ") or list(clients.keys())[0]
        product_idx = int(input("Номер товара из списка выше: ")) - 1
        qty = int(input("Количество: "))
        if products[product_idx]['stock'] < qty:
            print(f"Недостаточно остатка для {products[product_idx]['name']}")
            return
        order_id = len(orders) + 1
        orders.append({
            'id': order_id,
            'client': client_name,
            'items': [(products[product_idx]['name'], qty)],
            'total': products[product_idx]['price'] * qty
        })
        products[product_idx]['stock'] -= qty
        print(f"Заказ #{order_id} создан.")
    elif choice == '4':
        if not clients:
            print("Список клиентов пуст. Добавьте клиента через меню (выберите 2 для товара или введите имя вручную).")
            return
        for name in clients:
            print(f"- {name}")
    elif choice == '5':
        print("Выход из программы.")
        exit()

choice = show_menu()
if choice and choice.isdigit():
    handle_choice(choice, products, orders, clients)
