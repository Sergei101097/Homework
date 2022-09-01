def even_number():
    i = range(100)
    number(i)
def number(val):
    en = []
    odd_number = []
    for num in val:
        if num % 2 == 0:
            en.append(num)
        elif num % 2 == 1:
            odd_number.append(num)
    print("Кол-во четных чисел составило: ", len(en))
    print(en)
    print("Кол-во нечетных чисел сочтавило: ", len(odd_number))
    print(odd_number)

even_number()