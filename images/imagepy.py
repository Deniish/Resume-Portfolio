import cv2
from PIL import Image
import numpy as np

# Load the image
image_path = "F:\portfolioclone\images\home-banner3.png"
image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Edge detection
edges = cv2.Canny(image, 100, 200)

# Convert the images to PIL format for easier saving
gray_pil = Image.fromarray(gray_image)
blurred_pil = Image.fromarray(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
edges_pil = Image.fromarray(edges)

# Save the new images
gray_pil.save("F:\portfolioclone\images\gray_image.png")
blurred_pil.save("F:\portfolioclone\images\blurred_image.png")
edges_pil.save("F:\portfolioclone\images\edges_image.png")

print("Images have been saved successfully.")
