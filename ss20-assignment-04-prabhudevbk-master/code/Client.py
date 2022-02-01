import asyncio
import websockets

from threading import Threa


async def callback2():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        name = input("Enter your name : ")
        welcome = f"{name} joined"
        await websocket.send(welcome)
        while True:
            message = input(":")
            msg_snd = f"{name} : {message}"
            await websocket.send(msg_snd)


async def callback1():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        while True:
            incoming_message = await websocket.recv()
            print(f"{incoming_message}")

def between_callback1():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(callback2())
    loop.close()

def between_callback2():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(callback1())
    loop.close()

_thread1 = Thread(target=between_callback2)
_thread2 = Thread(target=between_callback1)
_thread1.start()       
_thread2.start()       