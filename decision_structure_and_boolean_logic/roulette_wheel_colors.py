a = int(input('Введите цифру от 0 до 36: '))

b = a % 2

if a == 0:
    print("зеленый")
elif 1 <= a <= 10 and b == 1:
    print("красный")
elif 1 <= a <= 10 and b  == 0:
    print("черный")
elif 11 <= a <= 19 and b  == 1:
    print("черный")
elif 11 <= a <= 19 and b  == 0:
    print("красный")
elif 19 <= a <= 28 and b == 1:
    print("красный")
elif 19 <= a <= 28 and b == 0:
    print("черный")
elif 29 <= a <= 36 and  b == 1:
    print("черный")
elif 29 <= a <= 36 and b == 0:
    print("красный")
else:
    print("ошибка ввода")