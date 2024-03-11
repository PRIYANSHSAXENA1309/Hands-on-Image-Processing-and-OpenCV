import cv2
cap =cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("E:\\practice\\output.avi",fourcc,20.0,(640,480))
output1=cv2.VideoWriter("E:\\practice\\output1.avi",fourcc,20.0,(640,480),0)
print("cap",cap)
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        # frame=cv2.resize(frame,(500,500))
        frame=cv2.flip(frame,0)
        frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("my video",frame)
        cv2.imshow("gray video",frame1)
        output.write(frame)
        output1.write(frame1)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
cap.release()
output.release()
output1.release()
cv2.destroyAllWindows()