import asyncio
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
    
    ds = bm.multiplex_socket(['dogeusdt@aggTrade'])
    gs = bm.depth_socket('BTCUSDT', depth=BinanceSocketManager.WEBSOCKET_DEPTH_20)

    # then start receiving messages
                  

    async with ds as tscm:
        i=0
        intervals = 3600
        
        start_loop = int(time.time())
        filenum = 0
        dict2 = {'time':[], 'quantity-bin-tx':[], 'price-bin-tx':[]}
        while True:
            res = await tscm.recv()
            
            res1 = res['data']
            print(res1)

                
        

            dict2['price-bin-tx'].append(res1['p'])
            dict2['quantity-bin-tx'].append(res1['q'])
            dict2['time'].append(res1['T'])



            if int(time.time()) > start_loop + intervals: #what happens after 'intervals' seconds
                # open file for writing
                filenum = filenum + 1 
                filename1 = 'C:\\firaas\\code\\files5\\binance-txs{}.txt'

                f = open(filename1.format(filenum),"w")
                # write file
                f.write( str(dict2) )
                # close file
                f.close()
                  
                intervals = intervals + 3600
                dict2 = {'time':[], 'quantity-bin-tx':[], 'price-bin-tx':[]}
              


            await client.close_connection()
    

while True:

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

        