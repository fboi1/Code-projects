import pandas as pd
import requests
import numpy as np
import time
address_list1 = []
address_list2 = []
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}
url = 'https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html'

#get first page - need to do this outside loop so    dfall = pd.concat([dfall,df1,df2]) in the loop works. (i.e without dfall declared beforehand it wont accept the argument)
r = requests.get(url, headers=header)
address_list1.append(pd.read_html(r.text, attrs = {'id': 'tblOne'}))
a = np.reshape(address_list1, (np.shape(address_list1)[2],np.shape(address_list1)[3]))

address_list2.append(pd.read_html(r.text, attrs = {'id': 'tblOne2'}))
b = np.reshape(address_list2, (np.shape(address_list2)[2],np.shape(address_list2)[3]))

df1 = pd.DataFrame(a)
df2 = pd.DataFrame(b)
dfall = pd.concat([df1,df2])
address_list1=[]
address_list2=[]
time.sleep(30)
#===============
for i in range(2,21,1):
    url = 'https://bitinfocharts.com/top-100-richest-bitcoin-addresses-%s.html'
    url = url % (i)
    r = requests.get(url, headers=header)
    address_list1.append(pd.read_html(r.text, attrs = {'id': 'tblOne'}))
    a = np.reshape(address_list1, (np.shape(address_list1)[2],np.shape(address_list1)[3]))

    address_list2.append(pd.read_html(r.text, attrs = {'id': 'tblOne2'}))
    b = np.reshape(address_list2, (np.shape(address_list2)[2],np.shape(address_list2)[3]))

    df1 = pd.DataFrame(a)
    df2 = pd.DataFrame(b)
    dfall = pd.concat([dfall,df1,df2])
    
    address_list1=[]
    address_list2=[]
    time.sleep(30)

dfall.to_csv('addresses.csv')
print(dfall)
