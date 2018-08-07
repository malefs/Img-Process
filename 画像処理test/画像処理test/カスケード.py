import cv2

cascade=cv2.CascadeClassifier("cascade.xml")


src=cv2.imread("img\image2.jpg")
src_greay= cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


cars=cascade.detectMultiScale(src_greay)

for x, y ,w,h, in cars:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("sad", src)
cv2.waitKey(0)