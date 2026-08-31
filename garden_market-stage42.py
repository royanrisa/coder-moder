# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: GardenMarket
import sys

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def print_colored(message, color_code):
    print(color(message, color_code))

def clear_screen():
    print("\033[2J\033[H")

def print_header(title):
    print("\n" + clear_screen())
    print_colored(f"╔══════════════════════════════════════════════╗", "36")
    print_colored(f"║  {title:^52}  ║", "36")
    print_colored(f"╚══════════════════════════════════════════════╝", "36")

def print_section(title):
    print_colored(f"\n── {title} ─────────────────────────────────", "33")

def print_row(label, value):
    print(f"  {label:<20} {value}")

def print_table(headers, rows):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    line = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    print(line)
    print(line.replace("-", "="))
    header_line = "|" + "|".join(str(h).center(w + 2) for h, w in zip(headers, col_widths)) + "|"
    print(header_line)
    print(line)

    for row in rows:
        cell_line = "|" + "|".join(str(cell).ljust(w + 2) for cell, w in zip(row, col_widths)) + "|"
        print(cell_line)
    print(line)

def print_success(msg):
    print_colored(f"  ✓ {msg}", "32")

def print_error(msg):
    print_colored(f"  ✗ {msg}", "31")

def print_warning(msg):
    print_colored(f"  ! {msg}", "33")

def print_info(msg):
    print_colored(f"  i {msg}", "36")

def print_disabled(msg):
    print_colored(f"  [disabled] {msg}", "1;37")

def print_menu():
    print_colored("  [1] Список товаров", "33")
    print_colored("  [2] Добавить товар", "33")
    print_colored("  [3] Список заказов", "33")
    print_colored("  [4] Добавить заказ", "33")
    print_colored("  [5] Список клиентов", "33")
    print_colored("  [6] Статистика", "33")
    print_colored("  [0] Выход", "31")
