def equation(a: int, b: int, c: int, d: int) -> float:
    if a < b:
        return "Ошибка: корень из отрицательного числа"
    if c == d:
        return "Ошибка: деление на ноль"
    return ((a - b) ** 0.5) / (c - d)
