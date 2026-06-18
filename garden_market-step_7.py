# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: GardenMarket
def sort_records(records, field='date', reverse=False):
    if field == 'date':
        return sorted(records, key=lambda x: x['created_at'], reverse=reverse)
    elif field == 'priority':
        priority_map = {'high': 0, 'medium': 1, 'low': 2}
        return sorted(records, key=lambda x: priority_map.get(x['priority'], 3), reverse=(not reverse))
    else:
        return sorted(records, key=lambda x: str(x[field]).lower(), reverse=reverse)
