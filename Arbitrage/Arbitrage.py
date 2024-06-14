import GraphTools
import ForexTools

exchange_codes =  [
    "USD",  # United States Dollar
    "EUR",  # Euro
    "JPY",  # Japanese Yen
    "GBP",  # British Pound Sterling
    "AUD",  # Australian Dollar
    "CAD",  # Canadian Dollar
    "CHF",  # Swiss Franc
    "CNY",  # Chinese Yuan
    "SEK",  # Swedish Krona
    "NZD",  # New Zealand Dollar
    "MXN",  # Mexican Peso
    "SGD",  # Singapore Dollar
    "HKD",  # Hong Kong Dollar
    "NOK",  # Norwegian Krone
    "KRW",  # South Korean Won
    "TRY",  # Turkish Lira
    "RUB",  # Russian Ruble
    "INR",  # Indian Rupee
    "BRL",  # Brazilian Real
    "ZAR",  # South African Rand
    "PLN",  # Polish Zloty
    "PHP",  # Philippine Peso
    "CZK",  # Czech Koruna
    "IDR",  # Indonesian Rupiah
    "MYR"   # Malaysian Ringgit
]

file_name = 'exchange_rates.csv'

ForexTools.download_exchange_matrix(file_name, exchange_codes)
loaded_graph = ForexTools.read_exchange_matrix_csv(file_name)

solution, negative_cycles = GraphTools.floyd_warshall_with_cycles(loaded_graph)

print("Distance matrix:")
GraphTools.printGraph(solution, exchange_codes)

print("Negative cycles:", len(negative_cycles))
for cycle in negative_cycles:
    cycle_named = [exchange_codes[i] for i in cycle]
    print("Negative cycle:", cycle_named, GraphTools.get_product_of_path(loaded_graph, cycle))
