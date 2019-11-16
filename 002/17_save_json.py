import json

cities = [
    {'rank': 1, 'city': 'city1', 'population': 24150000},
    {'rank': 2, 'city': 'city2', 'population': 23500000},
    {'rank': 3, 'city': 'city3', 'population': 21516000},
    {'rank': 4, 'city': 'city4', 'population': 14722100},
    {'rank': 5, 'city': 'city5', 'population': 14160467}
]

print(json.dumps(cities, ensure_ascii=False, indent=2))