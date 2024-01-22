import requests
import json
import time


# start_loop = time.time()
# txlist = list(rawmem['result'].keys())
# print(time.time()- start_loop)
filenum = 0
intervals = 9
start_loop = int(time.time())
dict1 = {'txid':[], 'time':[], 'fee':[], 'value':[]}
txlist = []
setlist = []
s = set(setlist)         #convert list to 'set' for faster checking for duplicates

url = "http://gee:*gee1*@127.0.0.1:22555"
payload1 = json.dumps({'jsonrpc':'1.0', 'id':'curltest', 'method':'getrawmempool', 'params': [True]})
headers = {
  'Content-Type': 'text/plain'
}





while True:
    
    getrawmempool = requests.request("POST", url, headers=headers, data=payload1)
    time.sleep(2)
    rawmem  = getrawmempool.json()

    for key in rawmem['result'].keys(): #for each txid
        if key not in s:            #if txid isn't in s already then add it to txlist and setlist
            txlist.append(key) #current batch of rawmempool txids that need to have values added on
            #s.add(key)
            setlist.append(key) #overall batch of txids that have been seen since the start
             
            dict1['txid'].append(key)
            dict1['time'].append(rawmem['result'][key]['time'])
            dict1['fee'].append(rawmem['result'][key]['fee'])
    s = set(setlist)
    print(setlist)



    for i in range(len(txlist)): #for each txid in txlist (current batch of txs)
        tx = txlist[i]
        payload2 = json.dumps({'jsonrpc':'1.0', 'id':'curltest', 'method':'getrawtransaction', 'params': [tx, True]})

        getrawtransaction = requests.request("POST", url, headers=headers, data=payload2)
        rawtx = getrawtransaction.json()
        
        
        total = 0
        for x in range(len(rawtx['result']['vout'])):
            total = total + rawtx['result']['vout'][x]['value']
        dict1['value'].append(total)     
    txlist = [] #after checking all the transactions clear the cache




    
    
    
    
    #after 1hr
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
                   
            intervals = intervals + 9
            dict1 = {'txid':[], 'time':[], 'fee':[], 'value':[]}
            
            print(time.time()- start_1) 
            setlist = setlist[-int((len(setlist))/2):]           
            s = set(setlist) # keep last half of the list
            print(setlist)
    print(len(s))
     
    #print('gee')