import asyncio 
import websockets
import pyaudio
# install pyaudio
# sudo apt-get install portaudio19-dev
# pip install pyaudio

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

print(frames, len(frames))

"""
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
"""