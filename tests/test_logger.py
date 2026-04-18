import sys
import os

# Подключаем путь к модулю B (папка module_B)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module_B')))

from logger import log_success

def test_log_success_message():
    """Тест: логирование успешной операции"""
    result = log_success("Test operation completed")
    assert "SUCCESS" in result, "Ошибка! В логе нет слова SUCCESS"
    assert "Test operation completed" in result, "Ошибка! В логе нет сообщения"
    print("Тест пройден: логирование работает")

def test_log_empty_message():
    """Тест: логирование пустого сообщения"""
    result = log_success("")
    # Проверяем, что пустое сообщение не ломает код
    assert True
    print("Тест пройден: пустое сообщение обработано")

if __name__ == "__main__":
    test_log_success_message()
    test_log_empty_message()
