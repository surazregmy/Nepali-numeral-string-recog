from scipy.misc import imread
import numpy as np
import pandas as pd
import os
import cv2;
from os.path import join, dirname, realpath

UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/images/')
UPLOAD_FOLDERC = join(dirname(realpath(__file__)),'templates/mulsegimages/')

img = imread(UPLOAD_FOLDERC+'digit_1_0_2.png',0)
imgr = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
im = cv2.cvtColor(imgr, cv2.COLOR_BGR2GRAY)
cv2.imwrite(UPLOAD_FOLDERC+"resized.png",im)