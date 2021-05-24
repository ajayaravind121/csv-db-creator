from cryptography.fernet import Fernet
import pandas as pd

class Crypter:
    def __init__(self, key_path=None):
        if not key_path:
            self.key = Fernet.generate_key()
            with open("secret.key", "wb") as f:
                f.write(self.key)
        else:
            with open(key_path, "rb") as f:
                self.key = f.read()
        self.fcrypt = Fernet(self.key)

    def _encrypt(self, record):
        input = bytes(record, 'utf-8')
        return self.fcrypt.encrypt(input).decode('utf-8')
    
    def _decrypt(self, record):
        input = bytes(record, 'utf-8')
        return self.fcrypt.decrypt(input).decode('utf-8')
    
    def encrypt_col(self, col:pd.Series):
        return col.apply(lambda x: self._encrypt(x))

    def decrypt_col(self, col:pd.Series):
        return col.apply(lambda x: self._decrypt(x))

