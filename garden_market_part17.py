# === Stage 17: Добавь группировку записей по категориям ===
# Project: GardenMarket
def group_by_category(records, key_field='category'):
    groups = {}
    for record in records:
        cat = record.get(key_field) or 'Uncategorized'
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(record)
    return list(groups.items())
