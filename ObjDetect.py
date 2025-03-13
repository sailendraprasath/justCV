import cv2
import numpy as np
import matplotlib.pyplot as plt

full = cv2.imread(r'E:\justCV\siberian_husky_2_.png')
full = cv2.cvtColor(full,cv2.COLOR_BGR2RGB)

face = cv2.imread(r'E:\justCV\siberian_husky_21_.png')
face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)

methods = ['cv2.TM_CCOEFF' ,'cv2.TM_CCOEFF_NORMED' , 'cv2.TM_CCORR' , 'cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF' ,'cv2.TM_SQDIFF_NORMED']

for m in methods:

    #Create A Copy
    full_copy = full.copy()
    method = eval(m)

    #Template Matching

    res = cv2.matchTemplate(full_copy,face,method)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    height, width , channel = face.shape
    bottom_right = (top_left[0]+width,top_left[1]+height)

    cv2.rectangle(img=full_copy,pt1=top_left,pt2=bottom_right,color=(255,0,0),thickness=4)


    plt.subplot(121)
    plt.imshow(res)
    plt.title('HEAT MAP OF TEMPLATE MATHCHING')

    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('DETECTION OF TEMPLATE')

    #Title with method used
    plt.suptitle(m)

    plt.show()

    print('\n')
    print('\n')


# plt.imshow(full)

# plt.show()


