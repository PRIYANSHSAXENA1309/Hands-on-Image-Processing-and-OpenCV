import cv2 
# colorfull or 3 channel
img=cv2.imread("E:\\avengers.jpg",1)
img=cv2.resize(img,(1280,700))
print(img)
cv2.imshow("window",img)

# greyscale or single channel
img1=cv2.imread("E:\\avengers.jpg",0)
img1=cv2.resize(img1,(1280,700))
print(img1)
cv2.imshow("window1",img1)

# increasing alpha channel or saturation
img2=cv2.imread("E:\\avengers.jpg",-1)
img2=cv2.resize(img2,(1280,700))
print(img2)
cv2.imshow("window2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()