import sys

# Функція для парсингу рядка логу
def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)  # Розділяємо рядок на частини: дата, час, рівень, повідомлення
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                logs.append(log_entry)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    return logs

# Функція для фільтрації логів за рівнем логування
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"] == level.upper()]

# Функція для підрахунку записів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        if level not in counts:
            counts[level] = 0
        counts[level] += 1
    return counts

# Функція для виведення результатів
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

# Основна функція скрипту
def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до файлу логів.")
        return

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    
    if not logs:
        print("Не вдалося завантажити логи.")
        return

    # Підрахунок і виведення статистики
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"Немає записів для рівня '{level_filter.upper()}'.")

if __name__ == "__main__":
    main()