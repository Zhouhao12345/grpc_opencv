import os
import cv2 as cv


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

def detect_face(img):
    cascade_fn = os.path.abspath(os.path.dirname(__file__)) + "/opencv/haarcascades/haarcascade_frontalface_alt.xml"
    nested_fn = os.path.abspath(os.path.dirname(__file__)) + "/opencv/haarcascades/haarcascade_eye.xml"

    cascade = cv.CascadeClassifier(cascade_fn)
    nested = cv.CascadeClassifier(nested_fn)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)

    rects = detect(gray, cascade)
    vis = img.copy()
    draw_rects(vis, rects, (0, 255, 0))
    if len(rects)>0:
        return True
    else:
        return False