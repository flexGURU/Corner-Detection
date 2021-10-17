#importing the openCV and the numpy libraries

import cv2
import numpy as np

#the image that we want to draw the corners on
image = cv2.imread('chess.jpg')

#for better image manipluation using python, the image is usually converted to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#call out the goodFeturesToTrack module in the CV2 library that detects the various corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 3)

#printing the number of corners
print(len(corners))

#the corners are usually in float-type, thus we need to make them as integers
corners = np.int0(corners)

#loopoing through the corners
for corner in corners:
    # flattening the corners
    x, y = corner.ravel()
    #drawing circles on the corners so that they are visible
    cv2.circle(image, (x,y),(5),(255,0,0),-1)

#displaying the image with marked corners
cv2.imshow('frame', image)
cv2.waitKey(0)
cv2.destroyAllWindows()