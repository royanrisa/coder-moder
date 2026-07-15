# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: GardenMarket
def show_order(order):
    print(f"Order #{order['id']}")
    print(f"Customer: {order['customer']['name']}")
    print("Items:")
    for item in order['items']:
        print(f"  - {item['product']['name']}: {item['quantity']}x")
    print(f"Total: ${sum(i['price']*i['quantity'] for i in order['items']):.2f}")

def show_product(product):
    print(f"Product #{product['id']}: {product['name']} (${product['price']:.2f}) - Stock: {product['stock']}")

def show_customer(customer):
    print(f"Customer #{customer['id']}: {customer['name']} (Orders: {len(customer['orders'])})")

print("Available functions:")
print("  show_order(order)    -> shows one order with customer and items")
print("  show_product(product) -> shows one product with stock")
print("  show_customer(customer) -> shows one customer with order count")
