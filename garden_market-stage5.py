# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: GardenMarket
def delete_record(table_name, record_id):
    if not table_name or not record_id:
        print("Ошибка: Идентификатор таблицы или записи отсутствует.")
        return False
    try:
        with open('database.txt', 'r+', encoding='utf-8') as f:
            lines = f.readlines()
        found = False
        new_lines = []
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) < 2: continue
            try:
                current_id = int(parts[0])
            except ValueError:
                current_id = float('inf')
            if str(current_id) == str(record_id):
                found = True
            else:
                new_lines.append(line)
        if not found:
            print(f"Запись с ID {record_id} не найдена в таблице '{table_name}'.")
            f.seek(0); f.truncate()
            f.writelines(new_lines)
        return True
    except Exception as e:
        print(f"Произошла ошибка при удалении: {e}")
        return False

# Пример вызова (раскомментируйте для теста):
# delete_record('products', '105')
