from keras.models import load_model
import numpy as np
import cv2
import time
from grabscreen import grab_screen
from getkeys import key_check
import pyautogui

#loading the model
model = load_model('dino.h5')
    
def main():

    for i in list(range(8))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # 640x480 windowed mode
            screen = grab_screen(region=(0,0,640,480))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen,(64,64))
            screen = screen[np.newaxis,:,:,np.newaxis]
            screen = np.array(screen)
            
            # model prediction
            y_prob = model.predict(screen)
            prediction = y_prob.argmax(axis=-1)
            
            
            if prediction == 1:
            # jump
                pyautogui.press('up')
                print('JUMP')
                #time.sleep(.07)
            elif prediction == 0:
                 print('CHILL')
                 # do nothing
            elif prediction == 2:
                 pyautogui.keyDown('down')
                 time.sleep(.5)
                 pyautogui.keyUp('down')
                 pyautogui.press('up')
                 print('DUCKS')
                 # duck
                 

        
main()       
