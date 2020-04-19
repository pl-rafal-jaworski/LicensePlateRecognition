import cv2
import matplotlib.pyplot as plt
import numpy as np


def getMostFrequentColor(src):
    img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    data = np.array(img)
    colors, count = np.unique(data.reshape(-1, data.shape[-1]), axis=0, return_counts=True)
    return colors[count.argmax()]

def generateContours(source):
    return cv2.Canny(source, 100, 200)

def generateBW(source):
    return cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)

def openImage(source):
    img_orig = cv2.imread(source)
    #return img_orig
    return cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)

def generateGaussianBlur(source, intensivity=5):
    return cv2.GaussianBlur(source, (intensivity, intensivity), cv2.BORDER_DEFAULT)

def showImage(source):
    cv2.imshow('image', source)
    cv2.waitKey(0)

def getMaskedPhotoRed(image):
    low_red = [0,0,0]
    up_red = [255,0,0]

    #mask_img = cv2.inRange(plt.hsv, low_red, up_red)
    #return cv2.bitwise_and(image, image, mask=mask_img)
    pass