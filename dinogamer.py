import pyautogui
import time
le = 30
xk = 480
yk = 240
xp = xk
yp = 213

while True: 
 cactus = pyautogui.screenshot(region=(xk,yk,le,1))
 jmp = False
 for i in range(0,le):
  pix=cactus.getpixel((i,0))
  if (jmp := jmp or (pix == (172,172,172))): break
 if jmp: 
  pyautogui.keyDown("space")
  pyautogui.keyDown("space")
  pyautogui.keyUp("space")
 ptero = pyautogui.screenshot(region=(xp,yp,le,1))
 sit = False
 for i in range(0,le):
  pix=ptero.getpixel((i,0))
  if (sit := sit or (pix == (172,172,172))): break
 if sit: 
  pyautogui.keyDown("down")
  time.sleep(0.5)
  pyautogui.keyUp("down")
