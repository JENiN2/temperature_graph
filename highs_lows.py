import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Чтение дат, температурных минимумов и максимумов из файла.
weather_file = 'data/sitka_weather_2014.csv'
with open(weather_file) as weather:
    reader = csv.reader(weather)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
        lows.append(int(row[3]))
        highs.append(int(row[1]))

# Нанесение данных на диаграму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# Закрашевает область между линиями.
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграмы.
plt.title('Daily Highs and Lows Temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
# Поворачивает подписи на оси X.
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
