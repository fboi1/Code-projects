import pandas as pd
#import cbpro
import requests

#c = cbpro.PublicClient()

from datetime import datetime
import time
import json



# order_book = c.get_product_order_book('ETH-USD')
# bids = pd.DataFrame(order_book['bids'])
# asks = pd.DataFrame(order_book['asks'])
# df3 = pd.merge(bids, asks, left_index=True, right_index=True)
# df3 = df3.rename({"0_x":"Bid Price","1_x":"Bid Size", "2_x":"Bid Amount",
#            "0_y":"Ask Price","1_y":"Ask Size", "2_y":"Ask Amount"}, axis='columns')
# print(df3.head())

#trades = pd.DataFrame(requests.get('https://api.pro.coinbase.com/products/ETH-USD/trades').json())
#trades1 = pd.DataFrame(requests.get('https://api.exchange.coinbase.com/products/ETH-USD/book').json())

filenum =0
run = True
#trades1 = pd.DataFrame(requests)
intervals = 7200
start_loop = int(time.time())

d = {'a':[], 'b':[], 'time':[], 'bid:asks':[]}
#aggregated (level 2):
while run == True:
    startTime = datetime.now()
    trades1 = requests.get('https://api.exchange.coinbase.com/products/BTC-USD/book?level=2', verify=False).json()
    bids = pd.DataFrame(trades1['bids'])
    asks = pd.DataFrame(trades1['asks'])
    df = pd.merge(bids, asks, left_index=True, right_index=True)
    

    #df = df.rename({"0_x":"Bid Price","1_x":"Bid Size", "2_x":"Bid Amount",
    #          "0_y":"Ask Price","1_y":"Ask Size", "2_y":"Ask Amount"}, axis='columns')
    

    df = df.apply(pd.to_numeric)
    

    df['bids'] = df['0_x'] * df['1_x'] * df['2_x']
    df['asks'] = df['0_y'] * df['1_y'] * df['2_y']

    df['time'] = int(time.time())
    d['time'].append(int(time.time()))
    
    print([df['bids'].sum()/df['asks'].sum()]) #bids : asks
    print(df.head())
    print(df.shape)

    

    d['b'].append(trades1['bids'][0])
    d['a'].append(trades1['asks'][0])
    d['bid:asks'].append(df['bids'].sum()/df['asks'].sum())
    #d['time'].append(df.iloc[[0],[8]])
    print(datetime.now() - startTime)
    if int(time.time()) > start_loop + intervals: #what happens after an hour
        filenum = filenum + 1
        filename = 'C:\\firaas\\code\\productbook{}.txt'
        print('============================================================')
        with open(filename.format(filenum), 'w') as convert_file:
            convert_file.write(json.dumps(d))
        intervals = intervals + 7200
        d = {'a':[], 'b':[], 'time':[], 'bid:asks':[]}


print(d)

bids = pd.DataFrame(d['b'])
asks = pd.DataFrame(d['a'])
timez = pd.DataFrame(d['time'])
df3 = pd.merge(bids, asks, left_index=True, right_index=True)
df4 = pd.merge(df3, timez, left_index=True, right_index=True)
print(df4.head())




  


 # #non aggregated (level 3):
# tradesn = requests.get('https://api.exchange.coinbase.com/products/ETH-USD/book?level=3').json()
# tradesn2 = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in trades1.items() ]))
# bids = pd.DataFrame(tradesn['bids'])
# asks = pd.DataFrame(tradesn['asks'])
# df2 = pd.merge(bids, asks, left_index=True, right_index=True)

# df2 = df2.rename({"0_x":"Bid Price","1_x":"Bid Size", "2_x":"id",
#            "0_y":"Ask Price","1_y":"Ask Size", "2_y":"id"}, axis='columns')

# print(df2.head())
# print(df2.shape)



