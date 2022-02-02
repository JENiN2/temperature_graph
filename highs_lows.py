import csv

from matplotlib import pyplot as plt

# Чтение максимальных температур из файла.
weather_file = 'data/sitka_weather_2014.csv'
with open(weather_file) as weather:
    reader = csv.reader(weather)
    header_row = next(reader)

    highs = []
    for row in reader:
        highs.append(int(row[1]))

print(highs)

# Нанесение данных на диаграму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# Форматирование диаграмы.
plt.title('Daily Highs Temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
