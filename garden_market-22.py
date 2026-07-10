# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: GardenMarket
def check_expired_reminders(self):
        expired = []
        for order in self.orders:
            if order.reminder and order.reminder < datetime.now():
                expired.append((order, order.reminder))
        return expired
