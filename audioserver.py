import asyncio
import websockets 

async def test(websocket) :
  print("ww")
  w = await websocket.recv()
  print(f'this is {w}')
  resback = 'got the message'
 
  #await websocket.send(resback)
  #print('sending back data')

async def main():
 async with websockets.serve(test, "localhost",
port = 8765, origins = [
"http://localhost:6080"
"wss://literate-yodel-qv4q9r94x9gg2xx4w-6080.app.github.dev"
]):
  await asyncio.Future()

if __name__ == "__main__":
 asyncio.run(main())