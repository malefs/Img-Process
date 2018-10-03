import cv2
import datetime
import numpy as np
from  time import sleep

cap = cv2.VideoCapture("20180426_161146.mp4")

while(input("")==False):
    pass

try:
 
    while(1):
        # フレームを取得
        ret, frame = cap.read()
        c=cv2.Canny(frame,200,300)
    
        cv2.imshow("SHOW COLOR IMAGE", c)
        cv2.imshow("Origin",frame)

        # qを押したら終了
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

except cv2.error:
    quit()

