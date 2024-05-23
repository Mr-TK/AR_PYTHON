import cv2 as cv
from cv2 import aruco
import numpy as np
marker_dict = aruco.getPredefinedDictionary (aruco.DICT_4X4_50)
param_markers = aruco.DetectorParameters()
cap = cv.VideoCapture("http://192.168.0.183:8080/video")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    grey_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    markers_corners, markers_id, reject = aruco.detectMarkers(grey_frame, marker_dict, parameters= param_markers)

    for corners in list(markers_corners):
        # print(ids, " ", corners)
        cv.polylines(frame, [corners.astype(np.int32)], True, (0, 255,255), 4, cv.LINE_AA)
        print(markers_id)
    cv.imshow("fame", frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv.destroyWindow()