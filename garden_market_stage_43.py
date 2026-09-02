# === Stage 43: Добавь пагинацию длинных списков ===
# Project: GardenMarket
def paginate(items, page_size=10):
    """Simple paginator yielding (offset, page_items) tuples."""
    for start in range(0, len(items), page_size):
        yield start, items[start:start+page_size]
