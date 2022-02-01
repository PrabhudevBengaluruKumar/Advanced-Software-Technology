#!/usr/bin/env python

# Server structure
# @author: 

import asyncio
import websockets

# !!! Make sure to read the documentation:
# https://websockets.readthedocs.io/en/stable/intro.html
# This library requires Python ≥ 3.6.1.

# This example could be useful to you:
# https://websockets.readthedocs.io/en/stable/intro.html#synchronization-example

async def leave(websocket):
    ''' Process users that leave from the chat room ''' 
    pass

async def join(websocket):
    ''' Process users that join a chat room '''
    pass

async def broadcast(room, message):
    ''' Sends a message to all users in a chat room '''
    pass

async def messenger(websocket, path):
    ''' websocket server coroutine, it handles each connection individually '''
    pass

# The address of the server is ws://localhost:8765
# you can test you logic using a websocket client
# https://www.websocket.org/echo.html
start_server = websockets.serve(messager, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
