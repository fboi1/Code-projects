import pandas as pd
import ast
import time
start_loop = int(time.time())

with open(r"C:\firaas\code\files2\ETH-info1.txt", "r") as data:
    dictionary = ast.literal_eval(data.read()) #loads in file as 'dictionary'
with open(r"C:\firaas\code\files2\productbook1.txt", "r") as data:
    proddict = ast.literal_eval(data.read()) #loads in file as 'dictionary'
with open(r"C:\firaas\code\files2\DOGE-info1.txt", "r") as data:
    dogedict = ast.literal_eval(data.read()) #loads in file as 'dictionary'
with open(r"C:\firaas\code\files2\txs1.txt", "r") as data:
    txdict = ast.literal_eval(data.read()) #loads in file as 'dictionary'

#load df's
df1 = pd.DataFrame(dictionary)
df2 = pd.DataFrame(proddict)
df3 = pd.DataFrame(dogedict)
df4 = pd.DataFrame()
df5 = pd.DataFrame(txdict)

#make df with the time range rows
df4['time'] = range(1662466862,1662470464) #initial df - double check some weird indexing here

#rename doge and eth price columns for easy distinction
df3 = df3.rename(columns={'price': 'price-doge', 'volb': 'volb-doge', 'volq':'volq-doge'})
df1 = df1.rename(columns={'price': 'price-ETH', 'volb': 'volb-ETH', 'volq':'volq-ETH'})

#sum the transactions that occur at the same time
df5['total-val'] = df5.groupby(['time'])['value'].transform('sum')
df5['total-fee'] = df5.groupby(['time'])['fee'].transform('sum')

#sum the productbook bids and asks at the same time
df2['Total-bid'] = df2.groupby(['time'])['sum-bid'].transform('sum')
df2['Total-ask'] = df2.groupby(['time'])['sum-ask'].transform('sum')



df2 = df2.drop_duplicates(subset=['time'])
df1 = df1.drop_duplicates(subset=['time'])
df3 = df3.drop_duplicates(subset=['time'])
df5 = df5.drop_duplicates(subset=['time'])

#product book bid:ask ratio 
df2['bid/ask'] = df2['Total-bid']/df2['Total-ask']


#reset index
df1 = df1.reset_index(drop=True)
df2 = df2.reset_index(drop=True)
df3 = df3.reset_index(drop=True)
df5 = df5.reset_index(drop=True)


df3 = df3.fillna(method='ffill')
#merge
df2=pd.merge(df4, df2, on='time', how='outer')
df2=pd.merge(df2, df1, on='time', how='outer')
df2=pd.merge(df2, df3, on='time', how='outer')
df2 = df2.fillna(method='ffill') #fill before tx's are merged because tx's shouldn't be merged
df2=pd.merge(df2, df5, on='time', how='outer')
df2['total-fee'] = df2['total-fee'].fillna(method='ffill') #tx fee can be merged
#reset index
df2 = df2.reset_index(drop=True)



#df2 = df2.fillna(method='ffill') #================================
#print (pd.isnull(df2['time'].iloc))

#remove columns
df2.pop('sum-bid')
df2.pop('sum-ask')
df2.pop('Total-bid')
df2.pop('Total-ask')
df2.pop('txid')
df2.pop('value')
df2.pop('fee')

#convert df from object to numeric
df2 = df2.apply(pd.to_numeric, errors = 'coerce')
#calculate doge price change as a new column
df2['change'] = df2['price-doge'].diff()



print(time.time()- start_loop)




df2 = df2.iloc[4:3602] #excluding whitespaces 
df2 = df2.fillna(0) #fill na values with 0's (when no transactions occur)
df2.to_csv('cleandcsv8.csv', float_format='%f') #convert to csv



# import numpy as np

# print((s := df2["time"] - np.arange(len(df2))).groupby(s).cumcount() + 1)
# print(df2['change'].tail())
