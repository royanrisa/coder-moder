# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: GardenMarket
class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name.strip()
        if not self.name or len(self.name) > 50: raise ValueError("Invalid product name")
        try:
            self.price = max(0.01, round(float(price), 2))
        except ValueError as e: raise TypeError(f"Price must be a number: {e}") from None
        if stock < 0: raise ValueError("Stock cannot be negative")
        self.stock = stock

class Customer:
    def __init__(self, name: str):
        self.name = name.strip()
        if not self.name or len(self.name) > 100: raise ValueError("Invalid customer name")
        self.orders_count = 0

def validate_order_input(order_data: dict) -> tuple[bool, str | None]:
    required_fields = ['product_name', 'quantity']
    for field in required_fields:
        if field not in order_data or not isinstance(order_data[field], str): return False, f"Missing {field}"
    
    product_name = order_data['product_name'].strip()
    try: quantity = int(order_data['quantity'])
    except ValueError: return False, "Quantity must be an integer string"
    if quantity <= 0: return False, "Quantity must be positive"
    
    if not product_name or len(product_name) > 50: return False, f"Invalid product name length"
    return True, None
