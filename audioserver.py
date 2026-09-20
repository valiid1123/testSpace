import asyncio
import websockets 

# start requirements
# gh codespace ports forward 8765:8765
# gh codespace ports visibility 8765:public

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
"http://localhost:6080",
"https://orange-rotary-phone-4qv7g4gvrwpp3555r-6080.app.github.dev",
"https://orange-rotary-phone-4qv7g4gvrwpp3555r-6080.app.github.dev/vnc_auto.html",
]):
  await asyncio.Future()

if __name__ == "__main__":
 asyncio.run(main())