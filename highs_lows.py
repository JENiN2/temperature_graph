import csv
from datetime import datetime
import argparse

from matplotlib import pyplot as plt

# Выбор для какого места отображать погоду.
parser = argparse.ArgumentParser(description='Creating Daily Highs and Lows Temperatures Diagram')
parser.add_argument('--place', type=int, choices=[1, 2],
                    help='Choose: 1 - Sitka, 2 - Death Valley', required=True)
args = parser.parse_args()
place = args.place

weather_file = ''
if place == 1:
    place = 'Sitka, Alaska'
    weather_file = 'data/sitka_weather_2014.csv'
elif place == 2:
    place = 'Death Valley, California'
    weather_file = 'data/death_valley_2014.csv'

# Чтение дат, температурных минимумов и максимумов из файла.
with open(weather_file) as weather:
    reader = csv.reader(weather)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        # Обработка исключений. Если в исходном файле будет пропушенны значения high/low, программа продолжит работу.
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f'{current_date} - Missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Нанесение данных на диаграму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# Закрашевает область между линиями.
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграмы.
plt.title(f'Daily Highs and Lows Temperatures, July 2014\n{place}', fontsize=24)
plt.xlabel('', fontsize=16)
# Поворачивает подписи на оси X.
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
