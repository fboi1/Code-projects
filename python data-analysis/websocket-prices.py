import json, time
from websocket import create_connection
from datetime import datetime
from datetime import datetime


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
         'btcusdt@miniTicker', 'ethusdt@miniTicker'
         ],
        "id": 1
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
intervals = 3600
start_loop = int(time.time())
filenum = 0
dict2 = {'time':[], 'sum-bid':[], 'sum-ask':[]}
dictBTC = {'time':[], 'price':[], 'volb':[], 'volq':[]}
dictETH = {'time':[], 'price':[], 'volb':[], 'volq':[]}
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
                 




    data3 = gs.recv()
    response3 = json.loads(data3)
    if i > 1 :
        print(response3['s'])
        if response3['s'] == 'BTCUSDT':
            dictBTC['price'].append(response3['c'])
            dictBTC['volb'].append(response3['v'])
            dictBTC['volq'].append(response3['q'])
            dictBTC['time'].append(int(str(response3['E'])[:10]))
        if response3['s'] == 'ETHUSDT':
            dictETH['price'].append(response3['c'])
            dictETH['volb'].append(response3['v'])
            dictETH['volq'].append(response3['q'])
            dictETH['time'].append(int(str(response3['E'])[:10])) 

        if int(time.time()) > start_loop + intervals: #what happens after 'intervals' seconds
            # open file for writing
            filenum = filenum + 1 
            filename1 = 'C:\\firaas\\code\\files\\productbook{}.txt'
            filename2 = 'C:\\firaas\\code\\files\\BTC-info{}.txt'
            filename3 = 'C:\\firaas\\code\\files\\ETH-info{}.txt'
            f = open(filename1.format(filenum),"w")
            # write file
            f.write( str(dict2) )
            # close file
            f.close()
            #btc
            f = open(filename2.format(filenum),"w")
            # write file
            f.write( str(dictBTC) )
            # close file
            f.close()
            #eth 
            f = open(filename3.format(filenum),"w")
            # write file
            f.write( str(dictETH) )
            # close file
            f.close()                       
            intervals = intervals + 3600
            dict2 = {'time':[], 'sum-bid':[], 'sum-ask':[]}
            dictBTC = {'time':[], 'price':[], 'volb':[], 'volq':[]}
            dictETH = {'time':[], 'price':[], 'volb':[], 'volq':[]} 
                        

    print(datetime.now() - startTime) 


