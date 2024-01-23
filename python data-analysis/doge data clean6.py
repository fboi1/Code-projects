from fileinput import filename
import pandas as pd
import ast
import time
start_loop = int(time.time())



filenum = 1
df4 = pd.DataFrame()
df6 = pd.DataFrame()
gee2 = df6.to_dict()
 #make df with the time range rows
df4['time'] = range(1662466862,1662592863) #initial df - double check some weird indexing here
filename1 = "C:\\firaas\\code\\files5\\ETH-info{}.txt"
filename2 = "C:\\firaas\\code\\files5\\productbook{}.txt"
filename3 = "C:\\firaas\\code\\files5\\DOGE-info{}.txt"
filename4 = "C:\\firaas\\code\\files5\\txs{}.txt"
filename5 = "C:\\firaas\\code\\files5\\binance-txs{}.txt"

firstch = 1664152122

while filenum < 118:
    with open(filename1.format(filenum), "r") as data:
        dictionary = ast.literal_eval(data.read()) #loads in file as 'dictionary'
    with open(filename2.format(filenum), "r") as data:
        proddict = ast.literal_eval(data.read()) #loads in file as 'dictionary'
    with open(filename3.format(filenum), "r") as data:
        dogedict = ast.literal_eval(data.read()) #loads in file as 'dictionary'
    with open(filename4.format(filenum), "r") as data:
        txdict = ast.literal_eval(data.read()) #loads in file as 'dictionary'
    with open(filename5.format(filenum), "r") as data:
        bintxs = ast.literal_eval(data.read()) #loads in file as 'dictionary'
     
    df4 = pd.DataFrame()   
    df4['time'] = range((firstch+(3600*(filenum-1)))-3,firstch+(3600*(filenum)))
    print(df4)
    #load df's
    df1 = pd.DataFrame(dictionary)
    df2 = pd.DataFrame(proddict)
    df3 = pd.DataFrame(dogedict)
    df5 = pd.DataFrame(txdict)
    df7 = pd.DataFrame(bintxs)



    df7['time'] = df7['time'].astype(str).str[:10]
    df7['time'] = df7['time'].astype(int)

    #rename doge and eth price columns for easy distinction
    df3 = df3.rename(columns={'price': 'price-doge', 'volb': 'volb-doge', 'volq':'volq-doge'})
    df1 = df1.rename(columns={'price': 'price-ETH', 'volb': 'volb-ETH', 'volq':'volq-ETH'})

    #sum the transactions that occur at the same time
    df5['total-val'] = df5.groupby(['time'])['value'].transform('sum')
    df5['total-fee'] = df5.groupby(['time'])['fee'].transform('sum')

    #multiply the price and quant of transactions
    #df7['totalbin-q'] = df5.groupby(['time'])['quantity-bin-tx'].transform('sum')
    #df7['totalnin-p'] = df5.groupby(['time'])['price-bin-tx'].transform('sum')
    df7 = df7.apply(pd.to_numeric, errors = 'coerce') #conv to numeric 
    df7['bin-tx-val'] = df7['price-bin-tx']*df7['quantity-bin-tx']
    print(df7)
    df7['total-bin-tx-val'] = df7.groupby(['time'])['bin-tx-val'].transform('sum')
    print(df7.columns.values) #drpp un needed columns
    df7 = df7.drop(columns  = ['quantity-bin-tx', 'price-bin-tx', 'bin-tx-val'])
    print(df7)

    #sum the productbook bids and asks at the same time
    df2['Total-bid'] = df2.groupby(['time'])['sum-bid'].transform('sum')
    df2['Total-ask'] = df2.groupby(['time'])['sum-ask'].transform('sum')



    df2 = df2.drop_duplicates(subset=['time'])
    df1 = df1.drop_duplicates(subset=['time'])
    df3 = df3.drop_duplicates(subset=['time'])
    df5 = df5.drop_duplicates(subset=['time'])
    df4 = df4.drop_duplicates(subset=['time'])
    df7 = df7.drop_duplicates(subset=['time'])

    #product book bid:ask ratio 
    df2['bid/ask'] = df2['Total-bid']/df2['Total-ask']


    #reset index
    df1 = df1.reset_index(drop=True)
    df2 = df2.reset_index(drop=True)
    df3 = df3.reset_index(drop=True)
    df5 = df5.reset_index(drop=True)
    df4 = df4.reset_index(drop=True)
    df6 = df6.reset_index(drop=True)
    df7 = df7.reset_index(drop=True)


    df3 = df3.fillna(method='ffill')
    #merge
    print(df4.tail(20))    
    df4=pd.merge(df4, df2, on='time', how='outer') #df4 loses some time rows
    print(df4.tail(20))    
    df4=pd.merge(df4, df1, on='time', how='outer')
    print(df4.tail(20))    
    print(df4.head(10))
    df4=pd.merge(df4, df3, on='time', how='outer')
    #????????????????????????
    # df4=pd.merge(df4, df2, on='time', how='outer')
    # df4=pd.merge(df4, df1, on='time', how='outer')
    # df4=pd.merge(df4, df3, on='time', how='outer')
    
    df4 = df4.fillna(method='ffill') #fill before tx's are merged because tx's shouldn't be merged to fill na with prev vals

    df4=pd.merge(df4, df5, on='time', how='outer')
    df4=pd.merge(df4, df7, on='time', how='outer')
    print(df4.keys())
    print(df4.tail(20))
    print(df4.head(20))
    df4['total-fee'] = df4['total-fee'].fillna(method='ffill') #tx fee can be merged

    #reset index
    df2 = df2.reset_index(drop=True)
    df4 = df4.reset_index(drop=True)
    df6 = df6.reset_index(drop=True)

    # l1=df6.values.tolist()
    # l2=df4.values.tolist()
    # for i in range(len(l1)):
    #     l1[i].extend(l2[i])
    # df6=pd.DataFrame(l1,columns=df6.columns.tolist()+df4.columns.tolist())

    # print(df6.head(20))
    # pd.options.display.max_columns = None
    # pd.options.display.max_rows = None
    print(df6.tail(10))
    print(df4.head(10))
    #df6 = df6.combine_first(df4)
    print(df6.tail())
    df6 = pd.concat([df6, df4])


    print(df4.tail(20))
    print(df6.head())
    print(df6.tail(10))
    
    
    


    #df2 = df2.fillna(method='ffill') #================================
    #print (pd.isnull(df2['time'].iloc))



    
    



    print(time.time()- start_loop)




    #df2 = df2.iloc[4:3602] #excluding whitespaces 
    
    filenum = filenum + 1
print(df6)
    #remove columns
df6.pop('sum-bid')
df6.pop('sum-ask')
df6.pop('Total-bid')
df6.pop('Total-ask')
df6.pop('txid')
df6.pop('value')
#df6.pop('fee')
print(df6.keys())
df6['total-val'] = df6.groupby(['time'])['total-val'].transform('sum')
df6['total-bin-tx-val'] = df6.groupby(['time'])['total-bin-tx-val'].transform('sum')

df6 = df6.drop_duplicates(subset=['time'])
df6 = df6.sort_values('time')
print(df6.keys())
df6[['bid/ask', 'price-ETH', 'volb-ETH', 'volq-ETH', 'price-doge','volb-doge', 'volq-doge', 'fee']] = df6[['bid/ask', 'price-ETH', 'volb-ETH', 'volq-ETH', 'price-doge','volb-doge', 'volq-doge', 'fee']].fillna(method='ffill')

#convert df from object to numeric
df6 = df6.apply(pd.to_numeric, errors = 'coerce')
#calculate doge price change as a new column
print(df6.keys())
df6['change'] = df6['price-doge'].diff()
df6 = df6.fillna(0) #fill na values with 0's (when no transactions occur)  
print(df6)  
df6.to_csv('cleandcsv30.csv', float_format='%f') #convert to csv without scientific notation



# import numpy as np

# print((s := df2["time"] - np.arange(len(df2))).groupby(s).cumcount() + 1)
# print(df2['change'].tail())
