# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: GardenMarket
def backup_data_file(data_file, backup_dir="backups"):
    """Создаёт резервную копию файла данных в указанной директории."""
    import os, shutil
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(data_file)}.backup_{timestamp}")
    shutil.copy2(data_file, backup_path)
    return backup_path
