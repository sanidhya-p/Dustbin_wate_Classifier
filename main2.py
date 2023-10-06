import os

import cv2
import cvzone
from cvzone.ClassificationModule import Classifier


cap= cv2.VideoCapture(0)
classifier=Classifier('Resources/Model/keras_model.h5','Resources/Model/labels.txt')

# waste images
imagesList = []
pathofwaste = "Resources/Waste"
pathlist = os.listdir(pathofwaste)
for path in pathlist:
    imagesList.append(cv2.imread(os.path.join(pathofwaste,path), cv2.IMREAD_UNCHANGED))

# bin images
imagesBinsList = []
pathofBins = "Resources/Bins"
pathlist = os.listdir(pathofBins)
for path in pathlist:
    imagesBinsList.append(cv2.imread(os.path.join(pathofBins,path), cv2.IMREAD_UNCHANGED))

imgarrow= cv2.imread("Resources/arrow.png",cv2.IMREAD_UNCHANGED)

classdis= {0:4,
           1:2,
           2:1,
           3:3,
           4:1}

while True:
    _, img = cap.read()
    imgResize=cv2.resize(img,(540,310))
    imgbackground = cv2.imread("C:/Users/DELL/Downloads/WasteWizard (4).png")

    prediction = classifier.getPrediction(img)
    print(prediction)
    classid=prediction[1]

    classidvbin=classdis[classid]
    overlay_width = imagesList[0].shape[1]
    imgbackground = cvzone.overlayPNG(imgbackground, imagesList[classid], (907, 100))

    imgbackground = cvzone.overlayPNG(imgbackground, imgarrow, (978, 320))

    imgbackground= cvzone.overlayPNG(imgbackground, imagesBinsList[classidvbin-1], (895, 374))

    imgbackground[166:166+310, 110:110+540]=imgResize
    # cv2.imshow("Image", img)
    cv2.imshow("BG",imgbackground)
    cv2.waitKey(1)