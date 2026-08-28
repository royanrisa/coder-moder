# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: GardenMarket
import argparse, sys

def main():
    parser = argparse.ArgumentParser(description="GardenMarket CLI")
    parser.add_argument("--add-product", nargs=2, type=str, help="Название и цена товара")
    parser.add_argument("--add-order", nargs=2, type=str, help="ID клиента и список товаров")
    parser.add_argument("--show-products", action="store_true", help="Показать все товары")
    parser.add_argument("--show-orders", action="store_true", help="Показать все заказы")
    parser.add_argument("--show-clients", action="store_true", help="Показать всех клиентов")
    parser.add_argument("--show-stock", action="store_true", help="Показать остатки")
    args = parser.parse_args()

    if args.add_product:
        name, price = args.add_product
        products.append({"name": name, "price": float(price), "stock": 0})
        print(f"Товар добавлен: {name} за {price}")
        return

    if args.add_order:
        client_id, items_str = args.add_order
        items = [i.strip() for i in items_str.split(",")]
        orders.append({"client_id": client_id, "items": items})
        print(f"Заказ добавлен клиенту {client_id}: {', '.join(items)}")
        return

    if args.show_products:
        for p in products:
            print(f"{p['name']}: {p['price']}, остаток: {p['stock']}")
        return

    if args.show_orders:
        for o in orders:
            print(f"Клиент {o['client_id']}: {', '.join(o['items'])}")
        return

    if args.show_clients:
        print("Клиенты:", [clients[i]['id'] for i in range(len(clients))])
        return

    if args.show_stock:
        for p in products:
            print(f"{p['name']}: остаток {p['stock']}")
        return

if __name__ == "__main__":
    main()
