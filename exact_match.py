import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# List of images
image_list = []
n = int(input("Enter number of images : "))
for i in range(0, n):
    ele = input()
    image_list.append(ele)

print("Image List is =>",image_list)

# Submit image path
submit_image_path = input("Enter the image path for match: ")

# Load and preprocess submit image
submit_image = cv2.imread(submit_image_path)
submit_image = cv2.cvtColor(submit_image, cv2.COLOR_BGR2GRAY)

best_match = None
best_ssim = -1

# Iterate over the list of images
for image_path in image_list:
    # Load and preprocess list image
    list_image = cv2.imread(image_path)
    list_image = cv2.cvtColor(list_image, cv2.COLOR_BGR2GRAY)

    # Compute SSIM
    similarity = ssim(submit_image, list_image)
    
    # Update best match
    if similarity > best_ssim:
        best_ssim = similarity
        best_match = image_path

# Display the best match
print("Best match:", best_match)
