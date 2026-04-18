def calculate(price, discount=0):
    """Расчёт цены со скидкой"""
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    return price * (1 - discount / 100)

# Пример использования
if __name__ == "__main__":
    price = 1000
    discount = 10
    result = calculate(price, discount)
    print(f"Цена со скидкой {discount}%: {result}")
