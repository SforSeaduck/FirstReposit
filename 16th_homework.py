import csv

def print_airports_in_ukraine(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            if row['iso_country'] == 'UA':
                print(row['name'])

print_airports_in_ukraine('C:/Users/vasyl/Desktop/FirstReposit/airport-codes_csv.csv')
