import asyncio 
import websockets
import pyaudio

async def sendMessage():
 uri = "ws://localhost:8765"
 async with websockets.connect(uri) as websocket :
  i = 0
  while True : 
   w = 't'
   if (i == 1):  
    w = 'e'
  
   await websocket.send(w)
   print(f'sending key {w}')
  
   i += 1
   if (i == 2): 
    break
   
    

if __name__ == "__main__":
 asyncio.run(sendMessage())