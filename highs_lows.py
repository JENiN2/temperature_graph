import csv

# Чтение максимальных температур из файла.
weather_file = 'data/sitka_weather_2014.csv'
with open(weather_file) as weather:
    reader = csv.reader(weather)
    header_row = next(reader)

    highs = []
    for row in reader:
        highs.append(row[1])

print(highs)
