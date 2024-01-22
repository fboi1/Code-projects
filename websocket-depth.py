import asyncio
import json
import time
from binance import AsyncClient, BinanceSocketManager
from websocket import create_connection, WebSocketConnectionClosedException


def mult(*args):
  result2 = []
  args = tuple(j for j in args[0])
 
  for num in args:
      result = 1 
      for item in num:
          result *=item 
      result2.append(result)
  return list(result2)

i=0



async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e  a trade socket
    
    ds = bm.multiplex_socket(['btcusdt@depth20@100ms'])


    # then start receiving messages
                  

    async with ds as tscm:
        i=0
        intervals = 5
        
        start_loop = int(time.time())
        filenum = 0
        dict2 = {'time':[], 'sum-bid':[], 'sum-ask':[]}
        while True:
            res = await tscm.recv()
            res1 = res['data']
            print(res1)
            i = i+1
    
            if i > 1 :
                    res1.pop('lastUpdateId', None)

                                        
                    result = []   # list of buy and ask total values (quantity * price)                         
                    for item in res1:
                        values = res1[item]
                        for i,value in enumerate(values):
                            values[i] = list(map(float,value))
                        result.append(mult(res1[item]))

                    
                    total_bid = sum(result[0]) #total bids value
                    total_ask = sum(result[1])#total asks value
                    dict2['sum-bid'].append(total_bid)
                    dict2['sum-ask'].append(total_ask)
                    dict2['time'].append(int(time.time()))
                    print(res1)
                    print(result)
                               

            if int(time.time()) > start_loop + intervals: #what happens after 'intervals' seconds
                # open file for writing
                filenum = filenum + 1 
                filename1 = 'C:\\firaas\\code\\files\\productbook{}.txt'
                f = open(filename1.format(filenum),"w")
                # write file
                f.write( str(dict2) )
                # close file
                f.close()
                #      
                intervals = intervals + 5            
                dict2 = {'time':[], 'sum-bid':[], 'sum-ask':[]}                

            await client.close_connection()
    

while True:

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

        