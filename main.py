def main(input: str) -> str:
    parts = input.split()
    if len(parts) != 3:
        raise ValueError("Неверный формат ввода. Ожидается: 'число операция число'.")
    try:
        a = int(parts[0])
        operation = parts[1]
        b = int(parts[2])
    except ValueError:
        raise ValueError("Оба числа должны быть целыми числами.")
    if not (1 <= a <= 10 and 1 <= b <= 10):
        raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно.")
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        result = a // b
    else:
        raise ValueError("Неизвестная операция. Доступные операции: +, -, *, /.")
    return str(result)
if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите выражение (число операция число): ")
            result = main(user_input)
            print(result)
        except Exception as e:
            print(f"Ошибка: {e}")
            break