# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: GardenMarket
class Reminder:
    def __init__(self, title, date):
        self.title = title
        self.date = date  # datetime.date или datetime.datetime

    def is_due(self):
        if not isinstance(self.date, datetime):
            return False
        today = datetime.now().date() if isinstance(self.date, datetime) else self.date
        return self.date <= today and (today - self.date).days <= 7

    @property
    def days_left(self):
        if isinstance(self.date, datetime):
            delta = self.date.date() - datetime.now().date()
        else:
            delta = self.date - date.today()
        return delta.days


def print_active_reminders(reminders_list):
    active = [r for r in reminders_list if r.is_due()]
    if not active:
        print("Никаких напоминаний не требуется!")
        return
    print(f"Напоминания ({len(active)}):\n")
    for i, r in enumerate(active, 1):
        days = r.days_left
        urgency = "⚠️ Срочно!" if abs(days) <= 2 else "📅 Скоро"
        print(f"{i}. [{urgency}] {r.title} — через {days} дн.")


# Пример использования:
if __name__ == "__main__":
    r1 = Reminder("Закрыть банки с огурцами", datetime(2025, 7, 1))
    r2 = Reminder("Поставить соль на шкафу", datetime.now())
    print_active_reminders([r1, r2])
