def caching_fibonacci():
    # Створюємо порожній кеш у вигляді словника
    cache = {}

    # Внутрішня функція для обчислення числа Фібоначчі
    def fibonacci(n):
        # Якщо n <= 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1
        if n == 1:
            return 1
        # Якщо n вже є в кеші, повертаємо його значення
        if n in cache:
            return cache[n]

        # Обчислюємо значення, якщо його немає в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Повертаємо обчислене значення
        return cache[n]

    # Повертаємо внутрішню функцію
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))