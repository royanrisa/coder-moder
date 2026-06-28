# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: GardenMarket
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query=None, fields=None):
        if not query or not fields:
            return list(self.data)
        
        query_lower = query.lower()
        results = []
        
        for item in self.data:
            match = False
            for field_name in fields:
                value = item.get(field_name, "")
                if isinstance(value, str):
                    if query_lower in value.lower():
                        match = True
                        break
            
            if match:
                results.append(item)
        
        return results

# Пример использования в классе GardenMarket
class GardenMarket(SearchFilter):
    def __init__(self):
        self.products = []
        self.orders = []
        self.clients = []
    
    def add_product(self, name, category, price, stock):
        self.products.append({"name": name, "category": category, "price": price, "stock": stock})
    
    def add_order(self, client_id, product_ids, total_price):
        self.orders.append({"client_id": client_id, "product_ids": product_ids, "total_price": total_price})
    
    def search_products(self, query=None, fields=["name", "category"]):
        return self.search(query, fields)
    
    def search_orders(self, query=None, fields=["client_id"]):
        return self.search(query, fields)
    
    def search_clients(self, query=None, fields=["name"]):
        return self.search(query, fields)

# Инициализация и тестирование поиска
market = GardenMarket()
market.add_product("Варенье", "Фрукты", 300.0, 50)
market.add_product("Кетчуп", "Овощи", 250.0, 30)
market.add_product("Соус", "Мясо", 400.0, 15)

print(market.search_products(query="варенье"))
print(market.search_products(query="овощи"))
