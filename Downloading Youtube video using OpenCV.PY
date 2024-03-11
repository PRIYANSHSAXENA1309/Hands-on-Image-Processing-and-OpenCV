import cv2,pafy
url="https://www.youtube.com/watch?v=yLBv7wygSC4"
data=pafy.new(url)
data=data.getbest(preftype="mp4")
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)
print("Check =",cap.isOpened())
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("E:\\practice\\output2.mp4",fourcc,20.0,(640,480))
output1=cv2.VideoWriter("E:\\practice\\output3.mp4",fourcc,20.0,(640,480),0)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        cv2.resize(frame,(640,480))
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Online video",frame)
        cv2.imshow("Online gray video",gray)
        output.write(frame)
        output1.write(gray)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
cap.release()
output.release()
output1.release()
cv2.destroyAllWindows()
