import pandas as pd
from fcrypt import Crypter



def save_to_db(conn, csv, table_name, secret_key=None):
    crypter = Crypter(key_path=secret_key)

    print("Storing CSV Records to DB....")
    if type(csv) != pd.DataFrame:
        df = pd.read_csv(csv)
    try:
        df['password'] = crypter.encrypt_col(df['password'])
        print("Passwords Found. Encrypting Passwords")
    except KeyError:
        print("No passwords found. Encryption not needed")

    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Successfully written CSV to DB table '{table_name}'!!!")

def read_db(conn, table_name, decrypt=False, secret_key=None):
    read_query = f"SELECT * FROM {table_name}"
    read_df = pd.read_sql_query(read_query, conn)
    if decrypt:
        crypter = Crypter(key_path=secret_key)
        read_df['password'] = crypter.decrypt_col(read_df['password'])
    return read_df
