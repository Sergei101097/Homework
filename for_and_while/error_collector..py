stop = 'Da'


while stop == 'Da':
    number_of_mistakes_1 = int(input('Кол-во ошибок ПН: '))
    number_of_mistakes_2 = int(input('Кол-во ошибок ВТ: '))
    number_of_mistakes_3 = int(input('Кол-во ошибок СР: '))
    number_of_mistakes_4 = int(input('Кол-во ошибок ЧТ: '))
    number_of_mistakes_5 = int(input('Кол-во ошибок ПТ: '))
    total_ny_mistake = number_of_mistakes_1 + number_of_mistakes_2 + number_of_mistakes_3 + number_of_mistakes_4 + number_of_mistakes_5
    print(f"Кол-во ошибок за неделю, составило  {total_ny_mistake}")
    stop = str(input("Если желаете продолжить введите 'Da': "))
