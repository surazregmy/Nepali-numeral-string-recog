from scipy.misc import imread
import numpy as np
import pandas as pd
import os
import cv2;
from os.path import join, dirname, realpath

UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/images/')
UPLOAD_FOLDERC = join(dirname(realpath(__file__)),'templates/mulsegimages/')

def mycam_to_gray(filename):


    img = cv2.imread(UPLOAD_FOLDER+filename)
    im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    myResult = cv2.inRange(im, 0, 100)

    cv2.imwrite(str(UPLOAD_FOLDER)+"thres_image.png", myResult);
    # print(myResult)
    #
    # img1 = cv2.imread(UPLOAD_FOLDER+'thres_image.png')
    # res = cv2.resize(img1, (32, 32), interpolation=cv2.INTER_AREA)
    #
    # res2 = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    # print("Hello It is result 2")
    # print(res2)
    #
    # cv2.imwrite(str(UPLOAD_FOLDER)+'resized_image.png', res2);


def gray_to_csv(rec_file):
    img = imread(UPLOAD_FOLDERC+rec_file,0)
    imgr = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
    im = cv2.cvtColor(imgr, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(UPLOAD_FOLDERC+"resized.png",im)
    cv2.imshow("image",im)
    cv2.waitKey(500)


    row, col = im.shape[:2]
    bottom = im[row - 2:row, 0:col]
    bordersize = 2
    border = cv2.copyMakeBorder(im, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize,
                                borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0])
    cv2.imwrite(str(UPLOAD_FOLDERC)+'border.png',border)


    value = border.flatten()
    new_name = rec_file.split('.')
    df = pd.DataFrame(value).T
    df = df.sample(frac=1)  # shuffle the dataset
    with open(str(UPLOAD_FOLDERC)+new_name[0]+'.csv', 'a') as dataset:
        df.to_csv(dataset, header=False, index=False)
    return new_name[0]+'.csv'





