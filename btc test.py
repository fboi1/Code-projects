import pandas as pd
import time
your_btc_address = '12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX' # Genesis Block
offset = 0
url = 'https://blockchain.info/address/%s/%s%s'
transactions_url = url % (your_btc_address,"?format=json&offset=", offset)
df = pd.read_json(transactions_url) # reads page
list = []
transactions = df['txs'] # gets transactions
while transactions.count() > 99: # until the items on the page are less than 99 (implies last page is reached)
    transactions_url = url % (your_btc_address,"?format=json&offset=", offset)
    df = pd.read_json(transactions_url)
    transactions = df['txs'] # gets transactions
    for i in range(transactions.count()): # for i = 0 to transations.count 'i.e. 100' .....
        print(transactions[i]["time"]) # outputs time at each index
        list.append(transactions[i]["time"])
    offset = offset + 100    
    time.sleep(11) # rate query limit is 10
print(len(list))    