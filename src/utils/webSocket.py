import websocket 

#pip install websocket_client

ws = websocket.WebSocket()
ws.connect("ws://192.168.0.103/test_connection")

ws.send("hello")

ws.close()