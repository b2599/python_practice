import sqlite3

conn = sqlite3.connect('top_cities.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS cities')

c.execute('''
    CREATE TABLE cities (
        rank integer,
        city text,
        population integer
    )
''')

c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1, 'city1', 24150000))
c.execute('INSERT INTO cities VALUES (:rank, :city, :population)',
          {'rank': 2, 'city': 'city2', 'population': 23500000})

c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', [
    {'rank': 3, 'city': 'city3', 'population': 21516000},
    {'rank': 4, 'city': 'city4', 'population': 14722100},
    {'rank': 5, 'city': 'city5', 'population': 14160467}
])

conn.commit()

c.execute('SELECT * FROM cities')

for row in c.fetchall():
    print(row)

conn.close()