import pyautogui
le=10
xk=465
yk=240
while True: 
 pic = pyautogui.screenshot(region=(xk,yk,le,1))
 jmp = False
 for i in range(0,le):
  pix=pic.getpixel((i,0))
  #print(pix)
  #jmp = jmp or (pix == (172,172,172))
  jmp = jmp or (pix != (32,33,36))
 if jmp: 
  print(pix)
  pyautogui.press("space")

