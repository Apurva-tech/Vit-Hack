import cv2
import numpy as np
# Load image, convert to grayscale, Otsu's threshold
img = cv2.imread('template4.jpeg')
#sresult = image.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,100,apertureSize = 3)
print(img.shape[1])
print(img.shape)
minLineLength=100
lines = cv2.HoughLinesP(image=edges,rho=0.1,theta=np.pi/300, threshold=250,lines=np.array([]), minLineLength=minLineLength,maxLineGap=100)

a,b,c = lines.shape
for i in range(a):
    cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
    cv2.imwrite('houghlines5.jpg',img)
