#Screenshot - I

#First we install PyAutoGUI in our terminal using command pip install PyAutoGUI

#importing pyautogui
import pyautogui
import time

def Screenshot():
    name=time.time() #So that we can get unique name with current date and time each time 
    name='C:/Users/Dell/Pictures/Screenshots/{}.png'.format(name) #Saves image in the desired location
    img=pyautogui.screenshot #For screenshot
    img.save(name) #Save image
    img.show() #Display the image

screenshot()