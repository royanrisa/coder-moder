# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: GardenMarket
def get_monthly_stats(start_date, end_date):
    stats = {}
    for date in range(int((end_date - start_date).days) + 1):
        current_date = start_date + timedelta(days=date)
        month_key = current_date.strftime('%Y-%m')
        if month_key not in stats:
            stats[month_key] = {'orders': 0, 'revenue': 0.0, 'products_sold': {}}
        
        for order in orders_list:
            if start_date <= order['date'] <= end_date and current_date == order['date']:
                stats[month_key]['orders'] += 1
                stats[month_key]['revenue'] += order['total_amount']
                for item in order['items']:
                    product_name = item['product']['name']
                    if product_name not in stats[month_key]['products_sold']:
                        stats[month_key]['products_sold'][product_name] = 0
                    stats[month_key]['products_sold'][product_name] += item['quantity']
    
    return stats

from datetime import timedelta
