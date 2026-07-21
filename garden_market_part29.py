# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: GardenMarket
SETTINGS = {
    "app_name": "GardenMarket",
    "currency_symbol": "$",
    "default_discount_pct": 0,
    "max_order_items": 10,
    "log_level": "INFO",
}


def get_setting(key: str, default=None):
    return SETTINGS.get(key, default)
