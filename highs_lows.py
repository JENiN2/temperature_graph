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
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# Форматирование диаграмы.
plt.title('Daily Highs and Lows Temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
