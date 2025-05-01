import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # ✅ Corrected import

# Load and preprocess images
cat4 = cv2.imread('CATS_DOGS/train/CAT/4.jpg')
cat4 = cv2.cvtColor(cat4, cv2.COLOR_BGR2RGB)

dog = cv2.imread('CATS_DOGS/train/DOG/2.jpg')
dog = cv2.cvtColor(dog, cv2.COLOR_BGR2RGB)

# Create an image data generator with augmentation
image_gen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.1,
    height_shift_range=0.1,
    rescale=1/255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Apply transformation to an image (e.g., dog)
transformed_dog = image_gen.random_transform(dog)


image_gen.flow_from_directory('CATS_DOGS/train')
# Show the transformed image
# plt.imshow(transformed_dog)
# plt.axis('off')
# plt.title("Augmented Image")
# plt.show()
