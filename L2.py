import cv2
import numpy as np

img1=cv2.imread("image1.jpg")
img2=cv2.imread("image2.jpg")

sum=cv2.addWeighted(img1,0.8,img2,0.2,0)
cv2.imshow("Background Merging",sum)
cv2.waitKey(0)
sub=cv2.subtract(img1,img2)
cv2.imshow("SUbtracting Merging",sub)
cv2.waitKey(0)



img=cv2.imread("pickachu.png",1)
resize=cv2.resize(img,(700,700))
cv2.imshow("Pika VVika",resize)
cv2.waitKey(0)

kernel=np.ones((11,11),np.uint8)
n=cv2.erode(img,kernel)
cv2.imshow("Blah",n)
cv2.waitKey(0)
#Gaussian Blur
#we use this mostly in machine learining pre processing steps
Gaussian=cv2.GaussianBlur(img,(17,17),0)
cv2.imshow("Gaussian Blur",Gaussian)
cv2.waitKey(0)
#Median Blur 
#It is used in digital processing it preserves edges but removes noise
median=cv2.medianBlur(img,27)
cv2.imshow("Median Blur",median)
cv2.waitKey(0)
#Bilateral Blur
#Only sharp edges are preserved
Bilater=cv2.bilateralFilter(img,27,3,27)
cv2.imshow("Bilateral Blur",Bilater)
cv2.waitKey(0)
#Border
border=cv2.copyMakeBorder(img1,100,100,100,100,cv2.BORDER_CONSTANT,value=100)
cv2.imshow("Border",border)
cv2.waitKey(0)

cv2.destroyAllWindows()
