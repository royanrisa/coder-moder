# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: GardenMarket
def edit_record(record_type, record_id, updates):
    if not isinstance(updates, dict) or len(updates) == 0:
        raise ValueError("Обновления должны быть словарем с ключами для изменения")
    
    target_list = {
        "products": products,
        "orders": orders,
        "clients": clients,
        "stock": stock
    }.get(record_type, [])

    if not isinstance(target_list, list):
        raise ValueError(f"Тип записи '{record_type}' не поддерживается для редактирования")

    index = next((i for i, item in enumerate(target_list) if item["id"] == record_id), None)
    
    if index is None:
        print(f"Запись с ID {record_id} не найдена в разделе '{record_type}'.")
        return False
    
    original_item = target_list[index].copy()
    for key, value in updates.items():
        if key not in original_item or key == "id":
            raise ValueError(f"Ключ '{key}' недоступен для редактирования или не существует в записи.")
        target_list[index][key] = value
    
    print(f"Запись с ID {record_id} успешно обновлена: {', '.join([f'{k}: {v}' for k, v in updates.items()])}")
    return True
