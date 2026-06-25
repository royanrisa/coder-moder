# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: GardenMarket
import json, os
DATA_FILE = "garden_market_data.json"
def save_state(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
def load_state():
    if not os.path.exists(DATA_FILE):
        return {"products": [], "orders": [], "clients": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"products": [], "orders": [], "clients": []}
