ridge_length = int(input('Длина гряды в (метрах):'))

space_size = int(input('Размер пространства в (метрах):'))

space_size_1 = int(input('Размер пространства между виноградными лозами в (метрах):'))

total = (ridge_length - 2 * space_size) / space_size_1

print(f"Количество виноградных лоз, которые поместятся на гряде составила {total} лоз")