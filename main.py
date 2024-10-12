def add(x, y):
    """Функция для сложения двух чисел."""
    return x + y


def calculator():
    print("Простой калькулятор")
    print("Доступная операция: Сложение")

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")


if __name__ == "__main__":
    calculator()