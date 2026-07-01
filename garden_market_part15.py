# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: GardenMarket
def get_weekly_stats(start_date: str, end_date: str) -> dict[str, float]:
    from datetime import date, timedelta
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    stats = {}
    current = start - timedelta(days=start.weekday())
    while current <= end + timedelta(days=6):
        week_start = current
        week_end = current + timedelta(weeks=1, days=-1)
        if week_end > end:
            week_end = end
        total_revenue = 0.0
        for order in orders.values():
            if order['date'] >= week_start and order['date'] <= week_end:
                total_revenue += sum(item['price'] * item['qty'] for item in order['items'])
        stats[week_start.isoformat()] = round(total_revenue, 2)
        current += timedelta(weeks=1)
    return stats
