import cv2
from os.path import join, dirname, realpath
import numpy as np
from matplotlib import pyplot as plt

UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/images/')
UPLOAD_FOLDERC = join(dirname(realpath(__file__)),'templates/mulsegimages/')

def apply_threshold(filenmae):
    img = cv2.imread(UPLOAD_FOLDER+filenmae,0)
    img = cv2.medianBlur(img,5)
    cv2.imwrite(UPLOAD_FOLDERC+"medblur.png",img)

    ret,th1 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)

    cv2.imwrite(UPLOAD_FOLDERC+"threshold.png",th1)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,115,14)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,115,14)
    # titles = ['Original Image', 'Global Thresholding (v = 127)',
    #             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    # images = [img, th1, th2, th3]

    # cv2.imwrite(UPLOAD_FOLDERC+"th1.png", th1)
    # cv2.imwrite(UPLOAD_FOLDERC+"th2.png", th2)
    # cv2.imwrite(UPLOAD_FOLDERC+"th3.png", th3)
    # exit(0);
    # for i in range(4):
    #     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]),plt.yticks([])
    # plt.show()
    # exit(0);

    # cv2.imshow("adaptive filtered",th2)
    # cv2.waitKey()
    inverted = 255 - th2
    cv2.imwrite(UPLOAD_FOLDERC+'inverted_final.png',inverted)

    blurred = cv2.medianBlur(inverted,9);
    # cv2.imshow("Inverted d",inverted);
    # cv2.waitKey()
    # cv2.imshow("medina blurred",blurred);
    # cv2.waitKey(10000)
    cv2.imwrite(UPLOAD_FOLDERC+'median_blurred.png',blurred)


# for i in range(r_inverted.shape[0]):
#     for j in range(r_inverted.shape[1]):
#          print(r_inverted[i][j],end="  ")
#     print("\n")
#
# print(r_inverted.shape[0])
# print(r_inverted.shape[1])

# median filter()


