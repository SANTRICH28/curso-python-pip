import csv

def read_csv(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data
