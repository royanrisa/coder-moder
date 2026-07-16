# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: GardenMarket
def parse_date(date_str):
    """Парсит дату в формате 'ДД.ММ.ГГГГ' или 'ДД/ММ/ГГГГ'. Возвращает datetime.date."""
    import re
    date_str = date_str.strip()
    if not date_str:
        raise ValueError("Дата не может быть пустой")
    
    # Проверяем формат DD.MM.YYYY или DD/MM/YYYY
    pattern = r'(\d{1,2})[./](\d{1,2})[./](\d{4})'
    match = re.match(pattern, date_str)
    
    if not match:
        raise ValueError(f"Неверный формат даты. Ожидается DD.MM.YYYY или DD/MM/YYYY (получено: {date_str!r})")
    
    day, month, year = int(match.group(1)), int(match.group(2)), int(match.group(3))
    
    # Валидация диапазона значений
    if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
        raise ValueError(f"Некорректные значения даты: день={day}, месяц={month}, год={year}")
    
    # Проверка через datetime для корректности (учитывает количество дней в месяцах)
    try:
        from datetime import date as DateType
        return DateType(year, month, day)
    except ValueError as e:
        raise ValueError(f"Дата {date_str} некорректна: {e}")

def format_date(date_obj):
    """Форматирует дату в 'ДД.ММ.ГГГГ'."""
    if date_obj is None:
        return "не задана"
    return date_obj.strftime("%d.%m.%Y")
