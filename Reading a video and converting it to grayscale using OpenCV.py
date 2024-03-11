import cv2

cap=cv2.VideoCapture("E:\\practice\\Sample.mp4")
print("cap",cap)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(500,500))
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("my video",frame)
    cv2.imshow("gray video",frame1)
    k=cv2.waitKey(25)
    if(k==ord('q')) & 0xff:
        break
cap.release()
cv2.destroyAllWindows()    