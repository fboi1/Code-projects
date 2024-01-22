from itertools import count
import pandas as pd
import time
your_btc_address = ['bc1qa5wkgaew2dkv56kfvj49j0av5nml45x9ek9hz6', 'bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h']
offset = 0
url = 'https://blockchain.info/address/%s/%s%s'
#transactions_url = url % (your_btc_address[0],"?format=json&offset=", offset) #######[[0]]
#df = pd.read_json(transactions_url) # reads page
list = []
list2 = []
list3 = []
list4 = []
listfordf = []
#transactions = df['txs'] # gets transactions
exit_while = False
#geetest = df['n_tx'][0] - 1

for i in range(len(your_btc_address)): #each loop takes the next address to query from the list of addresses
    offset = 0 # make offset 0 when new address loaded
    transactions_url = url % (your_btc_address[i],"?format=json&limit=5000&offset=", offset) #set url
    df = pd.read_json(transactions_url) # reads page
    transactions = df['txs'] # gets transactions
    while (transactions.count() > df['n_tx'][0] - 1 or transactions.count() > 4499) and exit_while == False: # until the items on the page are less than 4999 (implies last page is reached) or num of transactions on the page are less than total transactions overall - and until exit while is true
        
        for b in range(transactions.count()): # for i = 0 to transations.count 'i.e. 100' .....
            if transactions[b]["time"] < 1653609600:
                exit_while = True
                break
            
        
            print(transactions[b]["time"]) # outputs time at each index
            list.append(transactions[b]["time"]) #list of timestamp at each transaction
            list2.append(transactions[b]["balance"]) #list of balnce at same transaction
            list3.append(transactions[b]["hash"]) #list of hash key at same transaction
            list4.append(transactions[b]["result"])
            if b == df['n_tx'][0] - 1: #exit when it's reached the final transaction
                exit_while = True
                break
            #
            
        if df['n_tx'][0] > 5000:    
            offset = offset + 4500   # incriments offfset so page is reloaded with the next 100 transactions 
            transactions_url = url % (your_btc_address[i],"?format=json&limit=4500&offset=", offset) #-new-
            df = pd.read_json(transactions_url) # reads page
            transactions = df['txs'] # gets transactions
        time.sleep(11) #query rate  limit is 10 seconds
    exit_while = False
#make a dataframe with the timestamps and balance
data = pd.DataFrame(list, columns = ["time"])    
data["balance"] = list2  
data["hash"] = list3
data["result"] = list4
#===

# transform data to needs
data = data.drop_duplicates('hash') #drop duplicate occurrances of same hash (incase 2 of the same transactions were recorded)
data['total'] = data.groupby('time')['result'].transform('sum') #add result of same timestamps together
data = data.drop_duplicates('time') #drop duplicate occurrances at same timestamp
data = data.reset_index(drop=True) # reset the index because after removing duplicates it removed their index too leaving an index like 0,1,4,5,6 etc
data["change"] = data["balance"].diff() #make column 'change' to show change between balance after each timestamp

#print whole df:
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(data)

print(data.head())    



