# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: GardenMarket
def print_metrics():
    total_revenue = sum(order.total for order in all_orders)
    unique_customers = len(set(order.customer_id for order in all_orders if order.customer_id))
    avg_order_value = total_revenue / max(len(all_orders), 1)
    orders_per_customer = {cid: len([o for o in all_orders if o.customer_id == cid]) 
                           for cid in set(o.customer_id for o in all_orders if o.customer_id)}
    print(f"Total revenue: ${total_revenue:.2f}")
    print(f"Unique customers: {unique_customers}")
    print(f"Average order value: ${avg_order_value:.2f}")
    print(f"Orders per customer: {orders_per_customer}")
