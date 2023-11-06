import csv
import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host='74.208.230.203',
    user='janusipm',
    password='Sunflower$33ds',
    database='Pollux'
)
cursor = connection.cursor()

with open(f'products_upc.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        # Insert data
        sql = "INSERT INTO product (name, gtin) VALUES (%s, %s)"
        cursor.execute(sql, row)

connection.commit()
connection.close()


