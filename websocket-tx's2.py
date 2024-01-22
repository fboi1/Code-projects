import asyncio
import websockets
import json
from websocket import create_connection
import time
async def main():
    async with websockets.connect("wss://ws.blockchain.info/inv") as client:
        print("[main] Connected to wss://ws.blockchain.info/inv" )

        cmd = '{"op":"ping"}'
        print('[main] Send:', cmd)
        await client.send(cmd)
        print('[main] Recv:', await client.recv())

        gee = create_connection('wss://ws.blockchain.info/inv')  
        gee.send(json.dumps({"op": "unconfirmed_sub"}))
        print(gee.recv())
        i=0
        intervals = 3600
        start_loop = int(time.time())
        filenum = 0
        dict1 = {'time':[], 'value':[]}

        while True:

            data2 = gee.recv() #blockchain.info transacions
            response2 = json.loads(data2)

            
            print(response2['x']['time'])
            #transactions:
            total = 0
            for x in range(len(response2['x']['inputs'])):
                # print(response2['x']['inputs'][x]['prev_out']['value'])
                total = total + response2['x']['inputs'][x]['prev_out']['value']
                
                
            
            dict1['value'].append(total) 
            dict1['time'].append(response2['x']['time'])  


            if int(time.time()) > start_loop + intervals: #what happens after 'intervals' seconds
                    # open file for writing
                    filenum = filenum + 1 
                    
                    filename = 'C:\\firaas\\code\\files\\txs{}.txt'
                    
                    f = open(filename.format(filenum),"w")
                    # write file
                    f.write( str(dict1) )
                    # close file
                    f.close()
                        
                    intervals = intervals + 3600
                    dict1 = {'time':[], 'value':[]}   

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())