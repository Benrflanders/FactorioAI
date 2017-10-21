"""import numpy as np
from mss import mss
from PIL import Image

my_region = {'top': 100, 'left': 10,'width':400, 'height':780} #area of the screen to grab

sct = mss()

def get_game_screen(region=None):

    with mss() as sct:
        region = my_region
        output = 'sct-{top}x{left}_{width}x{height}.png'.format(**region)

        #grab the data
        sct_img = sct.grab(region)

        mss.tools.to_png(sct_img.rgb, sct_img.size, output)
        print(output)
        return output
        
    """
"""
    sct.get_pixels(mon)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("test",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
""" 


    #return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

"""
import sys
import os
import time
import cv2
import mss
import numpy as np

#use xdotool to resize factorio window
#xdotool search --onlyvisible --name factorio
#xdotool windowsize 44041287 600 320

training_file = os.path.join(os.path.expanduser(".."), "training_data.npy")



if os.path.isfile(training_file) == False:
    print("NOT A FILE")
    sys.exit()
    



with mss.mss() as sct:
    monitor = {'top': 65, 'left': 0, 'width': 800, 'height': 420}
    img_matrix = []
    img = np.array(sct.grab(monitor))
    while(True):
    #for _ in range(10000):
        # Get raw pizels from screen and save to numpy array
        img = np.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Save img data as matrix
        img_matrix.append(img)

        # Display Image
        cv2.imshow('Normal', img)

        #return img?

        #when training data gets too full
        print (len(img_matrix))
        if len(img_matrix) == 100:
            np.save('outfile.npy',img_matrix)
            print("saving")
            img_matrix = []
            break;
        
        # Press q to quit
        if cv2.waitKey(2)& 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
"""
    # Playback image movie from screencapture
    for img in img_matrix:
        cv2.imshow('Playback', img)
        time.sleep(1)
"""
