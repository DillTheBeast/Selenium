import cv2
from PIL import Image
import numpy as np

# Load the first image
image1 = cv2.imread('image1.jpg')

# Convert image1 to grayscale
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Load the second image
image2 = cv2.imread('image2.jpg')

# Convert image2 to grayscale
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Calculate the structural similarity index (SSIM) between the two images
ssim = cv2.compare_ssim(gray_image1, gray_image2)

# Print the SSIM score (higher values indicate more similarity)
print(f"SSIM Score: {ssim}")

# You can set a threshold to decide if the images are similar or not
threshold = 0.85  # Adjust this threshold as needed
if ssim > threshold:
    print("The images are similar.")
else:
    print("The images are not similar.")

# Optionally, you can display the grayscale images for visualization
cv2.imshow("Image 1 (Grayscale)", gray_image1)
cv2.imshow("Image 2 (Grayscale)", gray_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
