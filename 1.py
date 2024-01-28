import math

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")

    choice = input("Введите номер операции: ")

    if choice == '0':
        print("Выход из калькулятора.")
        break

    if choice in ('6', '7', '8', '9', '10'):
        num = float(input("Введите число: "))

    if choice == '1':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 + num2
    elif choice == '2':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 - num2
    elif choice == '3':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 * num2
    elif choice == '4':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: деление на ноль.")
            continue
    elif choice == '5':
        num1 = float(input("Введите число: "))
        num2 = float(input("Введите степень: "))
        result = num1 ** num2
    elif choice == '6':
        result = math.sqrt(num)
    elif choice == '7':
        result = math.factorial(int(num))
    elif choice == '8':
        result = math.sin(math.radians(num))
    elif choice == '9':
        result = math.cos(math.radians(num))
    elif choice == '10':
        result = math.tan(math.radians(num))
    else:
        print("Некорректный выбор операции. Попробуйте еще раз.")
        continue

    print("Результат: ", result)