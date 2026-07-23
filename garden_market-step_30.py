# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: GardenMarket
class ProfileManager:
    def __init__(self):
        self.profiles = {}
        self.current_profile_name = None

    def add_profile(self, name, role="user"):
        if not name or name in self.profiles:
            return False
        self.profiles[name] = {"name": name, "role": role}
        self.current_profile_name = name
        return True

    def switch_profile(self, name):
        if name and name in self.profiles:
            self.current_profile_name = name
            return True
        return False

    def get_current_profile(self):
        if not self.current_profile_name or self.current_profile_name not in self.profiles:
            return None
        return dict(self.profiles[self.current_profile_name])

    def get_all_profiles(self):
        return [dict(p) for p in self.profiles.values()]
