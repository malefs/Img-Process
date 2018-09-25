import cv2

orgmov=cv2.VideoCapture("20180426_161146.mp4")
orgmov.open()

e,img1=orgmov.read()

while(orgmov.grab()):
    img0=img1
    e , img1=orgmov.read()




