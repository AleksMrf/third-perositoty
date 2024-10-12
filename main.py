def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calculator():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")

    choice = input("Введите номер операции (1/2): ")

    if choice in ['1', '2']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
    else:
        print("Неверный ввод. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    calculator()