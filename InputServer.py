from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pyautogui 
import asyncio 

# run for upgrade
# python3 -m pip install --upgrade pip

# needed dependices 
# pip install uvicorn fastapi pyautogui

# create Xauthority 
# touch /home/codespace/.Xauthority
# generate display code 
# xauth generate :1 . trusted


# start requirements
# gh codespace ports forward 8000:8000
# gh codespace ports visibility 8000:public
# uvicorn InputServer:app --reload &
# uvicorn InputServer:app &
# --port 6080
# get mouse position


mousePosition = pyautogui.position()
screen = pyautogui.size()
keyA = ' https://fluffy-fiesta-vpp69q9jpjwqcrqv-6080.app.github.dev/vnc_auto.html'
print(mousePosition)
class mouseInput (BaseModel): 
 x: int = 0
 y: int = 0

class keyinput(BaseModel):
 key : str = ""
 ispressed : bool = False

app = FastAPI()
origins = [
    "http://127.0.0.1:6080",
    "http://localhost:5900",
    "http://localhost:6080/*",
    "http://localhost:6080/vnc_auto.html",
	keyA,
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
       # post request func for keyboard emulation 
       # listener for post request buttons gamepad button 
       
       # post request func for mouse emulation 
       # listener for gamepad axis 
  
  
  
@app.get("/")
def root(): 
  print("log")
  return { "w": "test"}
  
@app.get("/keyboardInputs")
def setkeyboardInput(key : str, ispressed : bool):
 print(key, ispressed)
 if (ispressed == True):
     pyautogui.keyDown(key)
	 
 else : 
     pyautogui.keyUp(key)
 pass
 
async def movemouse (x, y):
 await asyncio.sleep(0.1)
 pyautogui.move(nX, nY, 20)

 return
  
 
@app.get("/mouseInput")
def setmouseposition(x : int, y : int): 
 currentMousePosition = pyautogui.position()
 nX = x 
 nY = y
 if ((x + currentMousePosition.x) < 10 or (x + currentMousePosition.x > screen[0] - 10)):		
     nX = 0		
 if ((y + currentMousePosition.y) < 10 or (y + currentMousePosition.y > screen[1] - 10)):		
     nY = 0	
 movemouse(nX, nY)
 return [x, y]