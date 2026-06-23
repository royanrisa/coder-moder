# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: GardenMarket
def export_state_to_json():
    import json
    state = {
        "products": products,
        "orders": orders,
        "clients": clients,
        "inventory": inventory
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
