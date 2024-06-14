import requests
import csv 
KEY = "GET YOUR OWN KEY"

def get_price(KEY, currency):
    url = KEY + currency
    response = requests.get(url)
    data = response.json()

    return data['conversion_rates']

def download_exchange_matrix(filename, exchange_codes):
    exchange_rates = {}
    for code in exchange_codes:
        exchange_rates[code] = get_price(KEY, code)

    adjacency_matrix = [[0 for i in range(len(exchange_codes))] for j in range(len(exchange_codes))]

    for i in range(len(exchange_codes)):
        for j in range(len(exchange_codes)):
            if i == j:
                adjacency_matrix[i][j] = 1
            else:
                if exchange_codes[i] not in exchange_rates:
                    adjacency_matrix[i][j] = float('inf')
                else:
                    adjacency_matrix[i][j] = exchange_rates[exchange_codes[i]][exchange_codes[j]]

    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(adjacency_matrix)

def read_exchange_matrix_csv(filename = 'exchange_rates.csv'):
    adjacency_matrix = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            adjacency_matrix.append([float(x) for x in row])
    return adjacency_matrix

