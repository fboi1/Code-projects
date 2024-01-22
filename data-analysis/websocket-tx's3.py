from asyncore import dispatcher
import websocket
import _thread
import time
import rel
import json
import datetime
i=0
intervals = 3600
start_loop = int(time.time())
filenum = 0
dict1 = {'time':[], 'value':[]}
def on_message(ws, message):
    global i, intervals, start_loop, filenum, dict1
    #print(message)
    
    data2 = message #blockchain.info transacions
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
            
            filename = 'C:\\firaas\\code\\files2\\txs{}.txt'
            
            f = open(filename.format(filenum),"w")
            # write file
            f.write( str(dict1) )
            # close file
            f.close()
                   
            intervals = intervals + 3600
            dict1 = {'time':[], 'value':[]}

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    ws.send(json.dumps({"op": "unconfirmed_sub"})) 

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp('wss://ws.blockchain.info/inv',
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
                               

    ws.run_forever()  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()