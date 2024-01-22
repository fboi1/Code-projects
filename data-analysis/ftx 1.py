import websocket
import json

this = json.dumps({'op': 'subscribe', 'channel': 'orderbook', 'market': 'BTC-PERP'})

def on_open(wsapp):
    wsapp.send(this)

def on_message(wsapp, message):
    print(message)

wsapp = websocket.WebSocketApp("wss://ftx.com/ws/", on_message=on_message, 
on_open=on_open)
wsapp.run_forever()