from eth_account import Account
from datetime import datetime
import os 

class Wallet:
    """
    Class that is used to create, store and load wallets
    """
    def __init__(self) -> None:
        self.wallets = []

    def load_wallets(self, filename: str):
        """
        load wallets from file with private keys
        :filename: path to the file with private keys 
        """
        self.wallets.clear()

        with open(filename) as file:
            keys = list(map(lambda x: x.strip(), file.readlines()))

        for key in keys:
            self.wallets.append(Account.from_key(key))
        

    def create_wallets(self, filename: str = "", n: int = 1, keys_dir: str = "keys"):
        """
        generates private and public keys
        :filename: path to the file where keys will be saved 
        :n: number of keys to generate
        :keys_dir: directory where keys will be stored in case if filename doesn't provided
        """

        if not filename:
            if not os.path.isdir(keys_dir):
                os.mkdir(keys_dir)

            current_date = datetime.now().strftime('%Y-%m-%d')
            current_time = datetime.now().strftime('%H-%M-%S')
            filename = f"{keys_dir}/private_keys_{current_date}_{current_time}.txt"
        
        with open(filename, 'w') as file:
            for _ in range(n):
                self.wallets.append(Account.create()) 
                file.write(f"{self.wallets[-1].key.hex()}\n")


    def __iter__(self):
        for w in self.wallets:
            yield w 

if __name__ == "__main__":
    w = Wallet()
    w.create_wallets()
    for i in w:
        print(i.address)