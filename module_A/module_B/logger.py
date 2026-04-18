from datetime import datetime

def log_success(message):
    """Запись успешной операции в лог"""
    if not message:
        return "Warning: empty message"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] SUCCESS: {message}"
    print(log_entry)
    return log_entry

def log_error(message):
    """Запись ошибки в лог"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR: {message}"
    print(log_entry)
    return log_entry

# Пример использования
if __name__ == "__main__":
    log_success("Операция выполнена успешно")
    log_error("Произошла ошибка")
