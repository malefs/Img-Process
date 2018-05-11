import numpy as np
import cv2

while(True):
    cap = cv2.VideoCapture("20180426_161146.mp4")

    fps    = cap.get(cv2.CAP_PROP_FPS)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter('output.mp4', int(fourcc), fps, (int(width), int(height)))

    size=0.7
    while(cap.isOpened()):
        try:
            ret, frame = cap.read()
            edge = cv2.Canny(frame,200,100)
            edge=cv2.rectangle(edge,(int(int(width)*(1-size/2)),0),(int(width),int(height)),(0,255,0),cv2.FILLED)
            edge=cv2.rectangle(edge,(0,0),(int(int(width)*(size/2)),int(height)),(0,255,0),cv2.FILLED)
            edge=cv2.rectangle(edge,(0,0),(int(width),int(int(height)*(size/2))),(0,255,0),cv2.FILLED)
            edge=cv2.rectangle(edge,(0,int(int(height)*(1-size/2))),(int(width),int(height)),(0,255,0),cv2.FILLED)
            out.write(edge)
            cv2.imshow('frame',edge)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except:
            break

    out.release()
    cap.release()

cv2.destroyAllWindows()