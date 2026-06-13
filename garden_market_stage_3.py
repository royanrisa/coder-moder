# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: GardenMarket
class GardenMarket:
    def __init__(self):
        self.products = {}
        self.orders = []
        self.customers = {}
        self.inventory = {}

    def add_product(self, name: str, price: float) -> None:
        if not self.products.get(name):
            self.products[name] = {'name': name, 'price': price}
            self.inventory[name] = 0

    def add_customer(self, name: str) -> None:
        if not self.customers.get(name):
            self.customers[name] = {'name': name, 'orders_count': 0}

    def create_order(self, customer_name: str, product_name: str, quantity: int) -> dict | None:
        try:
            self.add_customer(customer_name)
            if not self.products.get(product_name):
                return None
            current_price = self.products[product_name]['price']
            total_cost = current_price * quantity
            old_stock = self.inventory.get(product_name, 0)
            new_stock = old_stock - quantity
            if new_stock < 0:
                raise ValueError("Недостаточно товара")
            order_id = len(self.orders) + 1
            order = {
                'id': order_id,
                'customer': customer_name,
                'product': product_name,
                'quantity': quantity,
                'total_cost': total_cost,
                'timestamp': __import__('time').time()
            }
            self.orders.append(order)
            self.customers[customer_name]['orders_count'] += 1
            if product_name in self.inventory:
                self.inventory[product_name] = new_stock
            return order
        except Exception as e:
            print(f"Ошибка при создании заказа: {e}")
            return None
