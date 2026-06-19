import pytest
from equation import equation

def test_success():
    assert equation(9, 5, 5, 3) == 1.0
    assert equation(25, 0, 10, 5) == 1.0

def test_negative_root():
    assert equation(3, 5, 10, 2) == "Ошибка: корень из отрицательного числа"

def test_division_by_zero():
    assert equation(10, 1, 5, 5) == "Ошибка: деление на ноль"

def test_both_errors():
    assert equation(2, 5, 4, 4) == "Ошибка: корень из отрицательного числа"
