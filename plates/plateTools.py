import heapq

import cv2
import matplotlib.pyplot as plt
import numpy as np
from joblib.numpy_pickle_utils import xrange
from sklearn.cluster import KMeans


def getMostFrequentColor2(src):
    # discontinued
    data = np.array(src)
    colors, count = np.unique(data.reshape(-1, data.shape[-1]), axis=0, return_counts=True)
    return colors[count.argmax()]


def generateContours(source):
    return cv2.Canny(source, 100, 200)


def generateBW(source):
    return cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)


def openImage(source):
    img_orig = cv2.imread(source)
    # return img_orig
    return cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)


def generateGaussianBlur(source, intensivity=5):
    return cv2.GaussianBlur(source, (intensivity, intensivity), cv2.BORDER_DEFAULT)


def showImage(source):
    cv2.imshow('image', source)
    cv2.waitKey(0)


def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


def find_histogram(source):
    source = source.reshape((source.shape[0] * source.shape[1], 3))
    clt = KMeans(n_clusters=3)  # cluster number
    clt.fit(source)

    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()
    # hist returns percentages
    # clt.cluster_centers_ returns corresponding colors

    '''
    print(hist*255)
    print(clt.cluster_centers_)
    bar=plot_colors2(hist, clt.cluster_centers_)

    plt.axis("off")
    plt.imshow(bar)
    plt.show()
    '''

    return [hist, clt.cluster_centers_]


def getColorsInPlate(source):
    percentage, colors = find_histogram(source)
    bgIndex, fgIndex = heapq.nlargest(2, xrange(len(percentage)), key=percentage.__getitem__)
    bg = colors[bgIndex]
    fg = colors[fgIndex]
    return [bg, fg]
