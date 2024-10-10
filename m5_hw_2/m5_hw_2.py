# Імпортуємо модуль регулярних виразів для пошуку чисел у тексті
import re
# Імпортуємо Callable для типізації функції
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r'\d+\.\d+|\d+', text)  # Використовуємо регулярний вираз для пошуку дійсних чисел у тексті.
    
    for number in numbers:
        yield float(number)  # Перетворюємо кожен рядок на дійсне число і повертаємо генератором

def sum_profit(text: str, func: Callable):
    return sum(func(text))  # Використовуємо вбудовану функцію sum для підсумовування значень генератора

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")