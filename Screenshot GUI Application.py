#Screenshot - I

#First we install PyAutoGUI in our terminal using command pip install PyAutoGUI

#We are adding button for taking screenshot and quitting the application
#For this, we use tkinter library, which is built in library of python

#importing pyautogui
import pyautogui
import time
import tkinter as tk

def Screenshot():
    name=time.time() #So that we can get unique name with current date and time each time 
    name='C:/Users/Dell/Pictures/Screenshots/{}.png'.format(name) #Saves image in the desired location
    img=pyautogui.screenshot #For screenshot
    img.save(name) #Save image
    img.show() #Display the image

root=tk.tk() #Initializing the root variable
frame=tk.frame(root) #Creating a frame
frame.pack() #It will create us an UI where we will add buttons

button-=tk.Button(frame,text="Take Screenshot",command=Screenshot) #Create the button,showing button in frame,adding text and whichfnction should it call
button.pack(side=tk.LEFT) #Show the button in left

close=tk.Button(frame,text="Close",action=close)
close.pack(side=tk.LEFT)

root.mainloop() #Run a loop so that it displays GUI continiously