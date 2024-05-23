from cv2 import aruco
import cv2 as cv
from cv2 import aruco
marker_dict = aruco.getPredefinedDictionary (aruco.DICT_4X4_50)
marker_size =  400 #pixel
for id in range(20):
    marker_image = aruco.generateImageMarker (marker_dict, id, marker_size)
    cv.imshow("ing",marker_image)
    cv.imwrite(f"markers/maarker_{id}.png", marker_image)
    cv.waitKey(0)
