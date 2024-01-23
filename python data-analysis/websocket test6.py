import asyncio
import json
import time
from binance import AsyncClient, BinanceSocketManager
from websocket import create_connection, WebSocketConnectionClosedException

async def main():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e  a trade socket
    
    ds = bm.multiplex_socket(['btcusdt@miniTicker', 'ethusdt@miniTicker', 'btcusdt@depth20@100ms'])
    # then start receiving messages
                  

    async with ds as tscm:
        while True:
            res = await tscm.recv()
            print(res)
            time.sleep(0.5)


            await client.close_connection()
    

while True:

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

        