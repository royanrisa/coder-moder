# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: GardenMarket
import json, sys

def load_initial_data(json_string: str) -> dict:
    data = json.loads(json_string)
    
    def normalize_item(item):
        return {
            "id": item["id"],
            "name": item["name"],
            "price": float(item.get("price", 0)),
            "stock": int(item.get("stock", 0))
        }
    
    def normalize_order(order):
        return {
            "id": order["id"],
            "client_id": order["client_id"],
            "items": [normalize_item(i) for i in order.get("items", [])],
            "status": order.get("status", "pending"),
            "total_price": sum(i["price"] * i["quantity"] for i in order["items"]) if order.get("items") else 0.0,
            "created_at": order.get("created_at")
        }
    
    def normalize_client(client):
        return {
            "id": client["id"],
            "name": client["name"],
            "phone": client.get("phone", ""),
            "address": client.get("address", "")
        }

    if not data:
        return {"products": [], "orders": [], "clients": []}
    
    products = [normalize_item(p) for p in data.get("products", [])]
    orders = [normalize_order(o) for o in data.get("orders", [])]
    clients = [normalize_client(c) for c in data.get("clients", [])]

    return {
        "products": products,
        "orders": orders,
        "clients": clients
    }
