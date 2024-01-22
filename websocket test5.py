import json, time
from threading import Thread
from websocket import create_connection, WebSocketConnectionClosedException
from datetime import datetime
import pandas as pd
from datetime import datetime
import numpy as np
import asyncio
#from colorama import init
#from termcolor import colored


ws = create_connection('wss://stream.binance.com:9443/ws')
ws.send(json.dumps({
        "method": "SUBSCRIBE",
        "params":
        [
         "btcusdt@depth20@100ms"
         ],
        "id": 1
        }))
gs = create_connection('wss://stream.binance.com:9443/ws')
gs.send(json.dumps({
        "method": "SUBSCRIBE",
        "params":
        [
         'btcusdt@miniTicker'
         ],
        "id": 1
        }))        
es =  create_connection('wss://ws.blockchain.info/inv')               
es.send(json.dumps({
  "op": "unconfirmed_sub"
}))


#//
def mult(*args):
  result2 = []
  args = tuple(j for j in args[0])
 
  for num in args:
      result = 1 
      for item in num:
          result *=item 
      result2.append(result)
  return list(result2)
# #//



i=0
dict1 = {'time':[], 'value':[]}
dict2 = {'time':[], 'sum-bid':[], 'sum-ask':[]}
while True:
    startTime = datetime.now() 
    data = ws.recv()
    response = json.loads(data)
    
    i = i+1
    
    if i > 1 :
      response.pop('lastUpdateId', None)

                           
      result = []   # list of buy and ask total values (quantity * price)                         
      for item in response:
          values = response[item]
          for i,value in enumerate(values):
              values[i] = list(map(float,value))
          result.append(mult(response[item]))

      
      total_bid = sum(result[0]) #total bids value
      total_ask = sum(result[1])#total asks value
      dict2['sum-bid'].append(total_bid)
      dict2['sum-ask'].append(total_ask)
      dict2['time'].append(int(time.time()))
                 

  
    #     print(df.head())
    #     print(df.shape)
    # print(response)





    data2 = es.recv() #blockchain.info transacions
    response2 = json.loads(data2)

    
    print(response2['x']['hash'])
    #transactions:
    total = 0
    for x in range(len(response2['x']['inputs'])):
        # print(response2['x']['inputs'][x]['prev_out']['value'])
         total = total + response2['x']['inputs'][x]['prev_out']['value']
         

    dict1['value'].append(total) 
    dict1['time'].append(response2['x']['time'])       
    
    #print(response2['x']['inputs'][0]['prev_out']['value'])   



    data3 = gs.recv()
    response3 = json.loads(data3)
    #print(response3)
    print(datetime.now() - startTime) 


