def equation(a: int, b: int, c: int, d: int) -> float:
    if a < b:
        return "Ошибка: корень из отрицательного числа"
    if c == d:
        return "Ошибка: деление на ноль"
    return ((a - b) ** 0.5) / (c - d)

if __name__ == "__main__":
    print("Обычный расчет:", equation(9, 5, 5, 3))  
    print("Ошибка корня:", equation(3, 5, 10, 2))  
    print("Деление на ноль:", equation(10, 1, 5, 5)) 
