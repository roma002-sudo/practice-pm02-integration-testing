import sys
import os

# Добавляем путь, чтобы импорт модуля сработал
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module_A')))

from calc import calculate

def test_normal_calculation():
    """Тест: обычный расчёт цены"""
    result = calculate(1000, 10)
    # Ожидаем 900 (1000 - 10%)
    assert result == 900.0, f"Ошибка! Ожидалось 900.0, а получили {result}"
    print("Тест 1 пройден: нормальный расчет")

def test_zero_discount():
    """Тест: скидка 0%"""
    result = calculate(500, 0)
    assert result == 500.0, f"Ошибка! Ожидалось 500.0, а получили {result}"
    print("Тест 2 пройден: скидка 0")

if __name__ == "__main__":
    test_normal_calculation()
    test_zero_discount()
