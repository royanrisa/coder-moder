# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: GardenMarket
def switch_profile():
    """Переключение активного пользовательского профиля."""
    print("\n=== Переключение профиля ===")
    for i, profile in enumerate(user_profiles):
        status = "✓" if profile["active"] else " "
        print(f"{status} Профиль {i+1}: {profile['name']} — {profile['role']}")
    
    choice = input("\nВведите номер профиля для активации (или 'q' для выхода): ").strip()
    if choice.lower() == 'q':
        return
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(user_profiles):
            user_profiles[idx]["active"] = True
            print(f"\n✓ Профиль активирован: {user_profiles[idx]['name']} ({user_profiles[idx]['role']})")
        else:
            print("Ошибка: неверный номер профиля.")
    except ValueError:
        print("Ошибка: введите число или 'q'.")
