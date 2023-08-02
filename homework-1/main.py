"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv


def csv_reader(file):
    tuples = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tuples.append(tuple(row.values()))

    return tuples


with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="cds543"
) as conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                        csv_reader("north_data/employees_data.csv"))
        cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)",
                        csv_reader("north_data/customers_data.csv"))
        cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                        csv_reader("north_data/orders_data.csv"))

conn.close()
