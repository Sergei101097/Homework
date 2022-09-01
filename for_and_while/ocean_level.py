OCEAN_LEVEL = 3.2
year = int(input('Укажите количество лет: '))

for kol_year in range(1,year + 1):
    ocean_level = kol_year * OCEAN_LEVEL
    print(kol_year, "год",'\t',"Урвоень воды в океане состовляет",format(ocean_level,'.1f'),'мм')