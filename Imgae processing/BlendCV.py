import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(r'E:\justCV\puppy.jpeg')
convertOrgImg1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2 = cv2.imread(r'E:\justCV\siberian_husky_2_.png')
convertOrgImg2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)


# Blending images
convertOrgImg1 = cv2.resize(convertOrgImg1,(550,950))
convertOrgImg2 = cv2.resize(convertOrgImg2,(550,950))

blended = cv2.addWeighted(src1=convertOrgImg1,alpha=0.5,src2=convertOrgImg2,beta=0.5,gamma=0)

plt.imshow(blended)
plt.show()
