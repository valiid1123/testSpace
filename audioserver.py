import asyncio
import websockets 
import pyaudio
import wave 
import json 
import numpy 
from base64 import b64encode, b64decode
"""
 start requirements
 gh codespace ports forward 8765:8765
 gh codespace ports visibility 8765:public
"""

Chunk = 1024
Format = pyaudio.paInt16
Channels = 2
Rate = 44100
Duration = 2

p = pyaudio.PyAudio()
stream = p.open(format = Format, 
                channels = Channels,
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

SoundCounter = 0
# create/pick wave file name and return the relative path
# folder name pickSound must be create in the same play as were the server is running 
SoundPicker = SoundCounter % 2
SoundFileType = ['a', 'b']
SoundName = SoundFileType[SoundPicker]
SoundPath = "./pickSound"+"sound"+SoundName
if (SoundCounter >= 2): 
 SoundCounter = 0

waveFile = wave.open(SoundPath, "wb")
waveFile.setnchannels(Channels)
waveFile.setsampwidth(p.get_sample_size(Format))
waveFile.setframerate(Rate)
waveFile.writeframes(b''.join(frames))
waveFile.close()

frame = []

file = open(SoundPath, 'rb')
waveData = file.read()
waveData = numpy.frombuffer(waveData, dtype ='int16')
waveData = waveData.tolist()
file.close()
SoundCounter += 1
print(waveData)

print("recorded audio")
async def test(websocket) :
  
  w = await websocket.recv()
  print(f'this is {w}')
  resback = 'got the message'
  
  package = {"type" : 'audio/wav', "data": waveData}
  await websocket.send(json.dumps(package))
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