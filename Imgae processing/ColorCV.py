import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'E:\justCV\puppy.jpeg')
convert_orginal = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

convert_orginal = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)


convert_orginal = cv2.cvtColor(img,cv2.COLOR_RGB2HLS)

plt.imshow(convert_orginal)
plt.show()