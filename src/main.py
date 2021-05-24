from os import read
import sqlite3
import pandas as pd
from fcrypt import Crypter


sql_con = sqlite3.connect("database/csv_database.db")
secret_key = 'secret.key'
csv_path = 'test/sample.csv'

crypter = Crypter(key_path=secret_key)
df = pd.read_csv(csv_path)

try:
    df['password'] = crypter.encrypt_col(df['password'])
except KeyError:
    print("No passwords found. Encryption not needed")

df.to_sql('csv_table', sql_con, if_exists='replace', index=False)


read_query = "SELECT * FROM csv_table"
read_df = pd.read_sql_query(read_query, sql_con)
print("Before decryption:")
print(read_df)

print("After Decryption")
try:
    read_df['password'] = crypter.decrypt_col(read_df['password'])
except KeyError:
    print("No passwords found. Decryption not needed")
print(read_df)

sql_con.close()