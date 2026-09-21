import asyncio
import websockets 
import pyaudio
import wave 
"""
 start requirements
 gh codespace ports forward 8765:8765
 gh codespace ports visibility 8765:public
"""

Chunk = 1024
Format = pyaudio.paInt16
Channel = 1 
Rate = 44100
Duration = 10

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

stream.stop_stream()
stream.close()
p.terminate()

w = wave.open("e.wav", "wb")
w.setnchannels(Channel)
w.setsampwidth(p.get_sample_size(Format))
w.setframerate(Rate)
w.writeframes(b''.join(frames))
w.close()

a = wave.open('e.wav', 'rb')
f = a.readframes(Chunk)
print(f)



print("recorded audio")
async def test(websocket) :
  
  w = await websocket.recv()
  print(f'this is {w}')
  resback = 'got the message'
  #print(frames)

  await websocket.send(f)
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