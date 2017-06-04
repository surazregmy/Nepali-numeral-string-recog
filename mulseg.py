import cv2
from os.path import join, dirname, realpath
from matplotlib import pyplot as plt

UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/mulsegimages/')

image = cv2.imread(UPLOAD_FOLDER+'final.jpg',0)

equ = cv2.equalizeHist(image)
myResult = cv2.inRange(image, 100, 170)
myResult2 = cv2.inRange(equ,100,170)
cv2.imshow("thres",myResult)

cv2.imwrite(str(UPLOAD_FOLDER)+'thres.png',myResult)

plt.subplot(3,2,1);plt.imshow(image,'gray')
plt.subplot(3,2,2);plt.imshow(equ,cmap='gray')
# plt.subplot(2,2,3);plt.imshow(myResult,cmap='gray')
plt.subplot(3,2,3).hist(image.flatten(),256,[0,256], color = 'r')
plt.subplot(3,2,4).hist(equ.flatten(),256,[0,256], color = 'r')
plt.subplot(3,2,5);plt.imshow(myResult,cmap='gray')
plt.subplot(3,2,6);plt.imshow(myResult2,cmap='gray')


plt.show()


cv2.waitKey(10000)

