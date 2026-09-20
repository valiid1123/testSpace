import asyncio
import websockets 
import pyaudio

# start requirements
# gh codespace ports forward 8765:8765
# gh codespace ports visibility 8765:public


Chunk = 1024
Format = pyaudio.paInt16
Channel = 1 
Rate = 44100
Duration = 1/2

p = pyaudio.PyAudio()
stream = p.open(format = Format, 
                channels = 1,
				rate = Rate,
				input = True,
				frames_per_buffer = Chunk)
frames = []
for i in range(0, int(Rate/Chunk * Duration)):
 data = stream.read(Chunk)
 frames.append(data)
frames = b''.join(frames)
print("recorded audio")

async def test(websocket) :
  
  w = await websocket.recv()
  print(f'this is {w}')
  resback = 'got the message'
  
  await websocket.send(frames, text=True)
  print('sending back data')
  

async def main():
 async with websockets.serve(test, "localhost",
port = 8765, origins = [
"http://localhost:6080",
"https://orange-rotary-phone-4qv7g4gvrwpp3555r-6080.app.github.dev",
"https://orange-rotary-phone-4qv7g4gvrwpp3555r-6080.app.github.dev/vnc_auto.html",
]):
  print("starting audio server")
  await asyncio.Future()

if __name__ == "__main__":
 asyncio.run(main())