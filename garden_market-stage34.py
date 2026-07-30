# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: GardenMarket
def create_record_from_template(template_name):
    templates = {
        "order": lambda: {"id": None, "customer_id": None, "items": [], "total": 0},
        "customer": lambda: {"id": None, "name": "", "phone": ""},
        "item_in_stock": lambda: {"id": None, "product_id": None, "quantity": 0},
    }
    if template_name not in templates:
        return None
    record = templates[template_name]()
    for key, value in record.items():
        if isinstance(value, str) and len(value) < 10:
            try:
                value = int(input(f"Введите {key}: "))
                if key == "quantity":
                    value = max(0, value)
            except ValueError:
                pass
    return record
