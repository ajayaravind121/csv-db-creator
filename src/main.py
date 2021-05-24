import sqlite3
import pandas as pd 
from process_csv import save_to_db, read_db


sql_con = sqlite3.connect("database/csv_database.db")

secret_key = 'secret.key'
csv_path = 'test/sample.csv'
table_name = 'sample'

print("Writing CSV to DB(sqllite3)")
save_to_db(
    conn= sql_con,
    csv=csv_path, 
    table_name=table_name,
    secret_key=secret_key
    )

print ("\n\nReading top records from DB without Decryption")
df = read_db(
    conn=sql_con,
    table_name=table_name
)
print(df.head())

print('\n\nReading DB with Decryption:')
df = read_db(
    conn=sql_con,
    table_name=table_name,
    decrypt=True,
    secret_key=secret_key
)
print(df.head())
