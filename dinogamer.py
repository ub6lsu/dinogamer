import pyautogui
le=10
xk=460
yk=240
while True: 
 pic = pyautogui.screenshot(region=(xk,yk,le,1))
 jmp = False
 for i in range(0,le):
  jmp = jmp or (pic.getpixel((i,0)) == (172,172,172))
 if jmp: 
  pyautogui.press("space")
 #print (pix)
