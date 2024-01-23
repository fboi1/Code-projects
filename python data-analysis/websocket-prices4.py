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
    
    ds = bm.multiplex_socket(['btcusdt@miniTicker', 'ethusdt@miniTicker'])
    gs = bm.depth_socket('BTCUSDT', depth=BinanceSocketManager.WEBSOCKET_DEPTH_20)

    # then start receiving messages
                  

    async with ds as tscm:
        i=0
        intervals = 5
        
        start_loop = int(time.time())
        filenum = 0
        dictBTC = {'time':[], 'price':[], 'volb':[], 'volq':[]}
        dictETH = {'time':[], 'price':[], 'volb':[], 'volq':[]}
        while True:
            res = await tscm.recv()
            res1 = res['data']
            print(res1)
            
                                               
            if res['stream'] == 'btcusdt@miniTicker' or res['stream'] == 'ethusdt@miniTicker':
                print(res1)
                if res1['s'] == 'BTCUSDT':
                    dictBTC['price'].append(res1['c'])
                    dictBTC['volb'].append(res1['v'])
                    dictBTC['volq'].append(res1['q'])
                    dictBTC['time'].append(int(str(res1['E'])[:10]))
                if res1['s'] == 'ETHUSDT':
                    dictETH['price'].append(res1['c'])
                    dictETH['volb'].append(res1['v'])
                    dictETH['volq'].append(res1['q'])
                    dictETH['time'].append(int(str(res1['E'])[:10]))

            if int(time.time()) > start_loop + intervals: #what happens after 'intervals' seconds
                # open file for writing
                filenum = filenum + 1 
                filename2 = 'C:\\firaas\\code\\files\\BTC-info{}.txt'
                filename3 = 'C:\\firaas\\code\\files\\ETH-info{}.txt'
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
                intervals = intervals + 5

                dictBTC = {'time':[], 'price':[], 'volb':[], 'volq':[]}
                dictETH = {'time':[], 'price':[], 'volb':[], 'volq':[]}                     


            await client.close_connection()
    

while True:

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

        