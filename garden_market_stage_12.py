# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: GardenMarket
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict):
            for key in ['products', 'orders', 'clients']:
                if key not in data:
                    raise ValueError(f"Missing required section: {key}")
        elif isinstance(data, list):
            raise ValueError("JSON root must be an object")
        return data
    except FileNotFoundError:
        print(f"[ERROR] File '{filepath}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON format in '{filepath}': {e}")
        return None
