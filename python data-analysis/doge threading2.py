import logging
import threading
import time
import concurrent.futures
import multiprocessing 

import requests
import json
url = "http://gee:*gee1*@127.0.0.1:22555"
def thread_function(txlist):
 for i in range(len(txlist)):
    print('')
    tx = txlist[i]
    payload = json.dumps({'jsonrpc':'1.0', 'id':'curltest', 'method':'getrawtransaction', 'params': [tx, True]})
    headers = {
  'Content-Type': 'text/plain'
}
    getrawtransaction = requests.request("POST", url, headers=headers, data=payload)
    z = getrawtransaction.json()
    print(z['result']['vout'])


def threadfunc2():
    print("no")
    for i in range(6):
        print(i)

        payload = json.dumps({'jsonrpc':'1.0', 'id':'curltest', 'method':'getrawmempool', 'params': [True]})
    headers = {
    'Content-Type': 'text/plain'
    }

    getrawmempool = requests.request("POST", url, headers=headers, data=payload)

    #print(getrawmempool.json())
    x = getrawmempool.json()
    z = list(x['result'].keys())
    return z    

if __name__ == "__main__":



    z = threadfunc2()

    print(z)


    process1 = threading.Thread(target=thread_function, args=(z,))
    process2 = threading.Thread(target=threadfunc2)
    process1.start()
    process2.start()
    process1.join()