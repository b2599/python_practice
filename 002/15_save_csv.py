import csv

with open('14_top_cities.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['rank', 'city', 'population'])

    writer.writerows([
        [1, 'city1', 24150000],
        [2, 'city2', 23500000],
        [3, 'city3', 21516000],
        [4, 'city4', 14722100],
        [5, 'city5', 14160467]
    ])