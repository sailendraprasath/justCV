import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chess = cv2.imread('Chess.jpg')
found,corners = cv2.findChessboardCorners(flat_chess,(7,7))
cv2.drawChessboardCorners(flat_chess,(7,7),corners,found)
plt.imshow(flat_chess)

plt.show()