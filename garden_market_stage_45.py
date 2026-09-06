# === Stage 45: Добавь восстановление из резервной копии ===
# Project: GardenMarket
import copy, os, random

def load_backup(path):
    """Восстанавливает резервную копию из JSON-файла."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return copy.deepcopy(data)
    except FileNotFoundError:
        print(f"Резервная копия не найдена: {path}")
        return None

def save_backup(current_state, path):
    """Сохраняет текущее состояние в резервную копию."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(current_state, f, ensure_ascii=False, indent=2)

def restore_from_backup():
    """Восстанавливает данные из последней резервной копии."""
    backup_path = 'garden_market_backup.json'
    if not os.path.exists(backup_path):
        print("Нет резервной копии для восстановления.")
        return False
    backup = load_backup(backup_path)
    if backup is None:
        return False
    print("Резервная копия успешно восстановлена!")
    return backup

def create_test_backup():
    """Создает тестовую резервную копию для проверки."""
    backup = {
        'products': [
            {'id': 1, 'name': 'Варенье', 'price': 300, 'stock': 100},
            {'id': 2, 'name': 'Оливье', 'price': 250, 'stock': 50},
            {'id': 3, 'name': 'Салат', 'price': 200, 'stock': 75},
        ],
        'customers': [
            {'id': 1, 'name': 'Иван', 'phone': '89001112233'},
            {'id': 2, 'name': 'Мария', 'phone': '89004445566'},
        ],
        'orders': [
            {'id': 1, 'customer': 1, 'items': [{'product': 1, 'qty': 2}], 'total': 600},
        ],
        'reserves': {
            'backup_date': '2024-01-15',
            'total_products': 3,
            'total_customers': 2,
            'total_orders': 1,
        }
    }
    save_backup(backup, 'garden_market_backup.json')
    print("Тестовая резервная копия создана!")
    return backup

if __name__ == '__main__':
    print("Тестирование восстановления из резервной копии...")
    test_backup = create_test_backup()
    restored = restore_from_backup()
    if restored:
        print(f"Восстановлено {len(restored['products'])} товаров, {len(restored['customers'])} клиентов и {len(restored['orders'])} заказов.")
    else:
        print("Восстановление не удалось.")
