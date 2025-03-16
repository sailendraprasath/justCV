import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image and convert to RGB
chess = cv2.imread('Chess.jpg')
chess = cv2.cvtColor(chess, cv2.COLOR_BGR2RGB)

# Convert to Grayscale
Gray_chess = cv2.cvtColor(chess, cv2.COLOR_RGB2GRAY)  # Fix: Convert from RGB, not BGR

# Convert to float32 for Harris Corner Detection
Gray = np.float32(Gray_chess)

# Apply Harris Corner Detection
dst = cv2.cornerHarris(src=Gray, blockSize=2, ksize=3, k=0.04)

# Dilate result to mark corners better
dst = cv2.dilate(dst, None)

# Mark corners in red
chess[dst > 0.01 * dst.max()] = [255, 0, 0]  # Ensure image is in RGB

# Show the image
plt.imshow(chess)
# plt.axis('off')  # Remove axes for better visualization
plt.show()
