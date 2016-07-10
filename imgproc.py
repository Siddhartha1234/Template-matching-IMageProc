import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils


img1 = cv2.imread('img.jpg',0)
img2=img1.copy()
template= cv2.imread('templ.jpg',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
        'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
i=1
res=[0]*6
min_val=[0]*6
max_val=[0]*6
min_loc=[0]*6
max_loc=[0]*6
W,H=img2.shape[::-1]
img = img2.copy()
method = eval(methods[1])

res[i] = cv2.matchTemplate(img,template,method)
template1=template.copy()
template1=imutils.resize(template1,width=w)

min_val[i], max_val[i], min_loc[i], max_loc[i] = cv2.minMaxLoc(res[i])
while(max_val[i]>max_val[i-1] or i==1):
    # Apply template Matchine
    i=i+1
    res[i] = cv2.matchTemplate(img,template1,method)
    w,h = template1.shape[::-1]
    w,h = (int(w/1.1),int(h/1.1))
    # # = int(template1.shape[0]/1.1)
    template=imutils.resize(template1,width=w,height=h)
    min_val[i], max_val[i], min_loc[i], max_loc[i] = cv2.minMaxLoc(res[i])
k=1
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if(k==4 or k==5):
    top_left = min_loc[i]
else:
    top_left = max_loc[i]
#w, h = template1.shape[::-1]
bottom_right = (top_left[0] + w, top_left[0] + h)
#w, h = template1.shape[::-1]
cv2.rectangle(img,top_left, bottom_right, 255, 2)
if(max_val[k]>0.1):
#    plt.subplot(121),plt.imshow(res[k],cmap = 'gray')
 #   plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(template1, cmap='gray')
    plt.title('Template1'), plt.xticks([]), plt.yticks([])
    plt.suptitle(methods[k])
else:
    print "Not Found"
plt.show()
print min_val[k],max_val[k]
w, h = template.shape[::-1]
img=img2.copy()
res[i] = cv2.matchTemplate(img,template,method)
template2=template.copy()
template2=imutils.resize(template2,width=w)
min_val[i], max_val[i], min_loc[i], max_loc[i] = cv2.minMaxLoc(res[i])
min_val[i-1], max_val[i-1], min_loc[i-1], max_loc[i-1] = min_val[i], max_val[i], min_loc[i], max_loc[i]
while(max_val[i]>=max_val[i-1]):
     # Apply template Matchine
    res[i] = cv2.matchTemplate(img,template,method)
    w = int(template2.shape[1] *1.1)
    h= int(template2.shape[0]*1.1)
    template2=imutils.resize(template2,width=w,height=h)
    min_val[i-1], max_val[i-1], min_loc[i-1], max_loc[i-1] = min_val[i], max_val[i], min_loc[i], max_loc[i]
    min_val[i], max_val[i], min_loc[i], max_loc[i] = cv2.minMaxLoc(res[i])
    print min_val[i],max_val[i]
k=0
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if(k==4 or k==5):
    top_left = min_loc[k]
else:
    top_left = max_loc[k]

bottom_right = (top_left[0] + w, top_left[0] + h)
w, h = template2.shape[::-1]
cv2.rectangle(img,top_left, bottom_right, 255, 2)
if(max_val[k]>0.8):
    plt.subplot(121),plt.imshow(res[k],cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(methods[k])
else:
    print "Not Found"
plt.show()
print min_val[k],max_val[k]