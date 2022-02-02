import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Чтение дат и максимальных температур из файла.
weather_file = 'data/sitka_weather_2014.csv'
with open(weather_file) as weather:
    reader = csv.reader(weather)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
        highs.append(int(row[1]))

# Нанесение данных на диаграму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Форматирование диаграмы.
plt.title('Daily Highs Temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
