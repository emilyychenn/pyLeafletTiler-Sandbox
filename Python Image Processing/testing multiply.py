import cv2
from PIL import Image

# Read the images
foreground = cv2.imread("./colored images/image1.png")
background = cv2.imread("./colored images/image6.png")
# alpha = cv2.imread("puppets_alpha.png")

# Convert uint8 to float
foreground = foreground
background = background

# # Normalize the alpha mask to keep intensity between 0 and 1
# alpha = alpha.astype(float) / 255
#
# # Multiply the foreground with the alpha matte
# foreground = cv2.multiply(alpha, foreground)
#
# # Multiply the background with ( 1 - alpha )
# background = cv2.multiply(1.0 - alpha, background)

# Add the masked foreground and background.
# outImage = cv2.add(foreground, background)
outImage = cv2.multiply(foreground, background)

# Display image
result = Image.fromarray(outImage)
result.show()
# cv2.imshow("outImg", outImage / 255)
