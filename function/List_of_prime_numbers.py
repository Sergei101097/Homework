def prime_num():
    lower_value = int(input("Please, Enter the Lowest Range Value: "))
    upper_value = int(input("Please, Enter the Upper Range Value: "))
    for number in range(lower_value, upper_value + 1):
        f(number)
def f (val):
    if val > 1 :
        for i in range(2, val):
            if (val % i) == 0:
                break
        else:
            print(val)
prime_num()