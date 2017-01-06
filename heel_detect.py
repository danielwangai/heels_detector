import numpy as np
import cv2
from matplotlib import pyplot as plt

# haarcascade

heels_cascade = cv2.CascadeClassifier('path_to_haarcascade_xml_file')

image = cv2.imread('path_to_test_image')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# plot histogram for grayscale image
plt.hist(gray.ravel(), 256, [0, 256]);
plt.show()

heels = heels_cascade.detectMultiScale(gray, 5.3, 2)
for (x,y,w,h) in heels:
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(250,200,20),1)
    roi_gray = gray[y:y, x:x]
    roi_color = image[y:y, x:x]


cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
