import csv
import sys
from datetime import datetime
import argparse

from matplotlib import pyplot as plt


class FileSelect:
    """Обрабатывает ввод с клавиатуры"""
    def get_argument(self):
        # Выбор для какого места отображать погоду.
        parser = argparse.ArgumentParser(description='Creating Daily Highs and Lows Temperatures Graph')
        parser.add_argument('--place', type=int, choices=[1, 2],
                            help='Choose: 1 - Sitka, 2 - Death Valley', required=False)
        args = parser.parse_args()
        place = args.place
        return place

    def get_input(self, place):
        # Если при запуске файла аргументы не получены, предоставляет выбор с помощью input.
        if place is None:
            try:
                print('\nCreating Daily Highs and Lows Temperatures Graph\n')
                place = int(input('Choose place: 1 - Sitka, 2 - Death Valley: '))
            except ValueError:
                print('Wrong value: invalid data type.')
                sys.exit()
            else:
                if place > 2 or place < 1:
                    print('Wrong value: out of range.')
                    sys.exit()
                else:
                    return place
        else:
            return place


def check_choice(place):
    # Проверяет, какое место было выбрано.
    if place == 1:
        place = 'Sitka, Alaska'
        weather_file = 'data/sitka_weather_2014.csv'
        return place, weather_file
    elif place == 2:
        place = 'Death Valley, California'
        weather_file = 'data/death_valley_2014.csv'
        return place, weather_file


def read_file(weather_file):
    # Чтение дат, температурных минимумов и максимумов из файла.
    with open(weather_file) as weather:
        reader = csv.reader(weather)
        header_row = next(reader)

        dates, highs, lows = [], [], []
        current_date = 0
        for row in reader:
            # Обработка исключений. Если в исходном файле будет пропушенны значения high/low,
            # программа продолжит работу.
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
        return dates, highs, lows


def render(dates, highs, lows):
    # Принимает обработанные данные, рисует на их основе график.
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # Закрашевает область между линиями.
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Форматирование графика.
    plt.title(f'Daily Highs and Lows Temperatures, 2014\n{place}', fontsize=24)
    plt.xlabel('', fontsize=16)
    # Поворачивает подписи на оси X.
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


if __name__ == '__main__':
    choose_file = FileSelect()
    place = choose_file.get_argument()
    place = choose_file.get_input(place)
    place, weather_file = check_choice(place)
    dates, highs, lows = read_file(weather_file)
    render(dates, highs, lows)
