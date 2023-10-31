import csv
import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host='host',
    user='xxxxx',
    password='xxxxxxxxxxxx',
    database='xxxxxxxx'
)
cursor = connection.cursor()

with open(f'marketplace_table.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        # Insert data
        sql = "INSERT INTO marketplace (code, full_name) VALUES (%s, %s)"
        cursor.execute(sql, row)

connection.commit()
connection.close()


