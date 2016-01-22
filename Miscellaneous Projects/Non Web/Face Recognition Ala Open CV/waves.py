import cv2
import os


try:
    import cPickle as pickle
except:
    import pickle

import scipy.spatial
from scipy.spatial import Delaunay
from ConvexHull import *
import numpy as np





def create_harr_classification_hull(image, casc_path, label = None):
    featureCascade = cv2.CascadeClassifier(casc_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    features = featureCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors= 5,
    minSize=(10, 10),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    points = []
    bias = 20
    for (x, y, w, h) in features:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)
        points.append([x,y])
        points.append([x + w,y])
        points.append([x,y + h])
        points.append([x + w,y + w])


    x = [x[0] for x in points]
    y = [x[1] for x in points]
    for x in points:
        cv2.circle(image, (int(x[0]),int(x[1])), 2, (255,0,0))

    rePoints = [(x[0],x[1]) for x in points]
    hull = convex_hull(rePoints)

    previous = hull[0]
    for x in hull:
        print previous,previous[0]
        cv2.line(image,(int(previous[0]),int(previous[1])),(int(x[0]),int(x[1])),(255,0,0),1)
        previous = x
    cv2.line(image,(int(previous[0]),int(previous[1])),(int(hull[0][0]),int(hull[0][1])),(255,0,0),1)
    return image


def tryMovStuff():
    # cap = cv2.VideoCapture.open('BloodDiamond.avi')
    cap = cv2.VideoCapture('BloodDiamond.avi')
    count = 0
    # while cap.isOpened():
    #     success, image = cap.read()
    #     if success:
    #         cv2.imwrite(os.path.join('data/temp/', '%d.png') % count, image)
    #         count += 1
    #     else:
    #         print "Break at count:", count
    #         break
    # cv2.destroyAllWindows()
    # cap.release()

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        print ret
        print frame
        # print len(ret), len(frame)
        # Our operations on the frame come here
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    print "oy"

    # capture = cv2.CaptureFromFile('data/avis/BloodDiamond.avi')
    # frames = []
    # for i in xrange(100):
    #     img = cv2.QueryFrame(capture)
    #     tmp = cv2.CreateImage(cv2.GetSize(img),8,3)
    #     cv2.CvtColor(img,tmp,cv2.CV_BGR2RGB)
    #     frames.append(np.asarray(cv2.GetMat(tmp)))
    # frames = np.array(frames)
    # return frames


# tryMovStuff()

image = cv2.imread("./data/grimace.jpg")

create_harr_classification_hull(image,"haar_cascades/haarcascade_frontalface_default.xml")
cv2.imshow("Faces found", image)
cv2.waitKey(0)


