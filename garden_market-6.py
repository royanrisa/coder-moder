# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: GardenMarket
def filter_records(records, filters=None):
    if not filters: return records
    result = []
    for r in records:
        match_status = (filters.get('status') is None) or (r.get('status') == filters['status'])
        match_category = (filters.get('category') is None) or (r.get('category') == filters['category'])
        match_tags = True
        if 'tags' in r and 'tags' in filters:
            req_tags = set(filters['tags'])
            item_tags = set(r['tags'])
            match_tags = not req_tags - item_tags
        if match_status and match_category and match_tags: result.append(r)
    return result
