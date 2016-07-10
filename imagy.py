import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils

img = cv2.imread('from/to/pic1.jpg',0)
img2 = img.copy()
template = cv2.imread('from/to/pic2.jpg',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list

meth = 'cv2.TM_CCOEFF_NORMED'
img = img2.copy()
method = eval(meth)
i=0
max_val= []
# Apply template Matching-
res = cv2.matchTemplate(img,template,method)
min_val, val, min_loc, max_loc = cv2.minMaxLoc(res)
max_val.append(val)
while (i==0 or max_val[i]>max_val[i-1] ) :
    w = int(w/1.1)
    h = int(h/1.1)
    template =imutils.resize(template,w,h)
    res = cv2.matchTemplate(img, template, method)
    i=i+1
    min_val, val, min_loc, max_loc = cv2.minMaxLoc(res)
    max_val.append(val)
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img,top_left, bottom_right, 255, 2)

#plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.subplot(121),plt.imshow(template,cmap = 'gray')
plt.title('Object to be searched'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(meth)
plt.show()

print min_val , max_val[i-1]
