import asyncio
import websockets
 
async def test():
    async with websockets.connect('wss://socketsbay.com/wss/v2/1/demo/') as websocket:
        await websocket.send("hello")
        response = await websocket.recv()
        print(response)
 
asyncio.get_event_loop().run_until_complete(test())