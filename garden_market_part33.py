# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: GardenMarket
def undo(self):
        """Откат последнего действия."""
        if not self.history:
            print("Нечего отменять.")
            return None
        
        last_action = self.history.pop()
        
        action_type, data = last_action
        
        if action_type == "order":
            order_id, client_id, product_id, qty, total_cost = data
            
            # Восстанавливаем остатки на складе
            for item in self.products:
                if item.id == product_id and item.stock >= qty:
                    item.stock += qty
                    break
            
            # Удаляем заказ из заказов клиента
            for order in client.orders:
                if order.order_id == order_id:
                    client.orders.remove(order)
                    break
            
            print(f"Отменён заказ #{order_id}. Остатки возвращены.")
        
        elif action_type == "client":
            client_id, name = data
            self.clients[client_id] = {"name": name, "orders": []}
            print(f"Клиент #{client_id} восстановлен: {name}")
        
        elif action_type == "product":
            product_id, name, price, stock = data
            for product in self.products:
                if product.id == product_id:
                    product.name, product.price, product.stock = name, price, stock
                    break
            print(f"Товар #{product_id} восстановлен: {name}")
        
        else:
            print("Неизвестное действие для отката.")
