import cv2
path=input("Enter the path of image")
print("entered path is",path)
img=cv2.imread(path,0)
img=cv2.resize(img,(700,700))
img=cv2.flip(img,-1)
cv2.imshow("your window",img)
'''
k=cv2.waitKey(0)
if(k==ord('s')):
    cv2.imwrite("E:\\output.png",img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
'''

cv2.waitKey(0)
cv2.destroyAllWindows()