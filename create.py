import cv2
from grabscreen import grab_screen
from getkeys import key_check
import os
import time



with open('actions.csv', 'w') as csv:

        x = 0
        c = 0
        d = 0
        t = 0
        if not os.path.exists(r'./images'):
            os.mkdir(r'./images')


        for i in list(range(8))[::-1]:
            print(i+1)
            time.sleep(1)

    
        while(True):

            # 640x480 windowed mode
            screen = grab_screen(region=(0,0,640,480))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (64,64))
            # resize to something a bit more acceptable for a CNN
            keys = key_check()
            if 'up' in keys:
                if c < 1000:#1000 denotes the no of images for jump action
                    cv2.imwrite('./images/frame_{0}.jpg'.format(x), screen)
                    csv.write('1\n')
                    print('jump dino')
                    x += 1
                    c += 1
            elif 'down' in keys:
                if d < 25:#25 denotes the no of images for down action
                    cv2.imwrite('./images/frame_{0}.jpg'.format(x), screen)
                    csv.write('2\n')
                    print('duck')
                    x += 1
                    d += 1
            else:
                if t < 1000:#1000 denotes the no of images for run action
                    cv2.imwrite('./images/frame_{0}.jpg'.format(x), screen)
                    csv.write('0\n')
                    print('run')
                    x += 1
                    t += 1


            if c == 1000 and t == 1000 and d==25:
                csv.close()
                cv2.destroyAllWindows()
                break                
        







