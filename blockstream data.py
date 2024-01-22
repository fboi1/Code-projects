import encodings
import pandas as pd
import json

list1 = ['a','b'] # timestamp
list2 = [] #transaction value


# transactions_url = 'https://blockchain.info/address/bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h/?format=json&limit=5000&offset=15000'
# df = pd.read_json(transactions_url, lines=True) 
# print(df.head())

import webbrowser

df = pd.read_json('https://blockchain.info/address/bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h/?format=json&limit=5000&offset=15010') 
print()