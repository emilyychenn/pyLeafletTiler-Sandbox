from PIL import Image
import cv2
import cmapy


# Read image.
img = cv2.imread("test_image.jpg")

# Colorize with OpenCV.
img_colorized = cv2.applyColorMap(img, cmapy.cmap("Purples_r"))

# Or: colorize directly with Cmapy (does the same thing).
img_colorized = cmapy.colorize(img, "Purples_r")

# Display.
cv2.imshow("Image", img_colorized)
colored_img = Image.fromarray(img_colorized)
colored_img.save("colorized_img.png", "PNG")