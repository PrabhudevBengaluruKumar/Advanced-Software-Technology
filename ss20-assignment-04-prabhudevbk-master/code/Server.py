from websocket_server import WebsocketServer

queue = [] 
def new_client(client, server):
    for i in queue:
        server.send_message_to_all(i)
    pass

def message_received(client, server, message):
    if len(queue) == 9:
        queue.pop(0)
        queue.append(message)
    else:
        queue.append(message)
    if len(message) > 200:
        message = message[:200]+'..'
    print("Client(%d) said: %s" % (client['id'], message))
    server.send_message_to_all(message)

def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])

PORT=8765
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
