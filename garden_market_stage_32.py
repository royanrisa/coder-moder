# === Stage 32: Добавь журнал действий пользователя ===
# Project: GardenMarket
class LogEntry:
    def __init__(self, action, detail=""):
        self.action = action
        self.detail = detail
    
    def to_str(self):
        return f"[{self.action}] {self.detail}"


class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, action, detail=""):
        self.entries.append(LogEntry(action, detail))

    def show_last(self, n=10):
        return [e.to_str() for e in self.entries[-n:]]

    @property
    def all(self):
        return [e.to_str() for e in self.entries]


log = ActionLog()
