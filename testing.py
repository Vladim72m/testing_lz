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

def test_root_of_zero():
    assert equation(5, 5, 10, 5) == 0.0

def test_negative_inputs():
    assert equation(-2, -6, -3, -5) == 1.0

def test_float_result():
    assert equation(10, 6, 8, 4) == 0.5
