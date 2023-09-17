import time
import pyautogui
import win32api
import win32con
import sys




time.sleep(4)
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
def main():
    start_time = time.time()
    while time.time() - start_time < 21600 :
        pyautogui.moveTo( x= 507, y= 452)  # num 2222
        click()
        time.sleep(10)
            
        #################################>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        bton1 = pyautogui.locateCenterOnScreen("3.png",region=(0,0,1680,1050),grayscale=True, confidence=0.70)
        if bton1 is not None:
            pyautogui.moveTo( x= 1627, y= 118)
            click()
            time.sleep(10)
            pyautogui.moveTo( x= 797, y= 505)
            click()
            time.sleep(10)
            continue
            #################################>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        pyautogui.moveTo( x= 661, y= 745)  # num 33333
        click()
        time.sleep(12)
        ################################>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        bton2 = pyautogui.locateCenterOnScreen("4.png",region=(0,0,1680,1050),grayscale=True, confidence=0.70)
        bton2_2 = pyautogui.locateCenterOnScreen("5.png",region=(0,0,1680,1050),grayscale=True, confidence=0.70)
        if bton2 or bton2_2 is not None:
            pyautogui.moveTo( x= 1635, y= 99)
            click()
            time.sleep(10)
            pyautogui.moveTo( x= 840, y= 487)
            click()
            time.sleep(13)
            continue
        #################################>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        pyautogui.moveTo( x= 973, y= 657)  # num 4444
        click()
        time.sleep(10)
    
        pyautogui.moveTo( x= 390, y= 615)  # num 5555
        click()
        time.sleep(10)
        pyautogui.moveTo( x= 889, y= 604)   # num 6666
        click()
        time.sleep(7)
        
        pyautogui.moveTo( x= 1645, y=63 )   # rutern
        click()
        time.sleep(18)
        pyautogui.moveTo( x= 880, y= 440)   # num 1111
        click()
        time.sleep(8)
    sys.exit()
if __name__ == "__main__":
    main()
    
