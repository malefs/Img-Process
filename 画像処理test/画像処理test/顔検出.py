import cv2

img=cv2.imread("sad.jpg")

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)

face=faceCascade.detectMultiScale(gray,1.1,3)

if len(face) > 0:
    for rect in face:
        cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)
else:
    print("no face")