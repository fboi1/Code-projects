
import requests
import json
import time


# start_loop = time.time()
# txlist = list(rawmem['result'].keys())
# print(time.time()- start_loop)
filenum = 0
intervals = 3600
start_loop = int(time.time())
dict1 = {'txid':[], 'time':[], 'fee':[], 'value':[]}
txlist = []

url = "http://gee:*gee1*@127.0.0.1:22555"
payload1 = json.dumps({'jsonrpc':'1.0', 'id':'curltest', 'method':'getrawmempool', 'params': [True]})
headers = {
  'Content-Type': 'text/plain'
}


s = set(txlist)         #convert list to 'set' for faster checking for duplicates




while True:
    
    getrawmempool = requests.request("POST", url, headers=headers, data=payload1)
    time.sleep(2)
    rawmem  = getrawmempool.json()

    for key in rawmem['result'].keys():
        if key not in s:            #if txid isn't in txlist already then add it to txlist
            txlist.append(key)
            s.add(key)
            dict1['txid'].append(key)
            dict1['time'].append(rawmem['result'][key]['time'])
            dict1['fee'].append(rawmem['result'][key]['fee'])
    



    for i in range(len(txlist)):
        tx = txlist[i]
        payload2 = json.dumps({'jsonrpc':'1.0', 'id':'curltest', 'method':'getrawtransaction', 'params': [tx, True]})

        getrawtransaction = requests.request("POST", url, headers=headers, data=payload2)
        rawtx = getrawtransaction.json()
        
        
        total = 0
        for x in range(len(rawtx['result']['vout'])):
            total = total + rawtx['result']['vout'][x]['value']
        dict1['value'].append(total)     
    txlist = [] #after checking all the transactions clear the cache

    if int(time.time()) > start_loop + intervals: #what happens after 'intervals' seconds
            start_1 = time.time()
                    # open file for writing
            filenum = filenum + 1 
            
            filename = 'C:\\firaas\\code\\files2\\txs{}.txt'
            
            f = open(filename.format(filenum),"w")
            # write file
            f.write( str(dict1) )
            # close file
            f.close()
                   
            intervals = intervals + 3600
            dict1 = {'txid':[], 'time':[], 'fee':[], 'value':[]}
            print(time.time()- start_1) 


    print(len(s))
    print(time.time()- start_loop)   
    #print('gee')