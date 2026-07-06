# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: GardenMarket
def archive_records():
    """Archive completed or old records."""
    global all_ingredients, all_orders, all_customers
    for ingredient in list(all_ingredients):
        if ingredient['status'] == 'sold' and (date.today() - ingredient.get('created', date.today())).days > 30:
            ingredient['archive_date'] = date.today()
    for order in list(all_orders):
        if order['status'] == 'completed':
            order['archive_date'] = date.today()
    for customer in list(all_customers):
        if customer['last_order']['date'] and (date.today() - customer['last_order']['date']).days > 180:
            customer['archive_date'] = date.today()
