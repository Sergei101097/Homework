import  math
i = int(input("введите сек: "))

SEC_1 = 3600
if  i <= SEC_1:

    min = i / 60
    min_total = math.floor(min)
    min_total_vs_sec = min_total * 60
    total_sec = i - min_total_vs_sec
    print(min_total,'мин :',total_sec,"сек")



