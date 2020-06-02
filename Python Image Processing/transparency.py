# testing multiply blend mode

# open cv actually can't be used in this case since we need to convert images to RGBA (not rgb or brg)
import cv2

from PIL import Image
import blend_modes
import numpy as np

img1 = Image.open('./colored images/image1.png')
imgrgba1 = img1.convert("RGBA")
img1arr = np.array(imgrgba1)
image1_float = img1arr.astype(float)  # Inputs to blend_modes need to be floats

img2 = Image.open('./colored images/image6.png')
imgrgba2 = img2.convert("RGBA")
img2arr = np.array(imgrgba2)
image2_float = img2arr.astype(float)  # Inputs to blend_modes need to be floats

img3 = Image.open('./colored images/image4.png')
imgrgba3 = img3.convert("RGBA")
img3arr = np.array(imgrgba3)
image3_float = img3arr.astype(float)  # Inputs to blend_modes need to be floats


multiply_img = blend_modes.multiply(image1_float, image2_float, 1)
multiply2_img = blend_modes.multiply(multiply_img, image3_float, 1)
uint8_img = np.uint8(multiply2_img) # Image needs to be converted back to uint8 type for PIL handling.
final_img = Image.fromarray(uint8_img)
final_img.show()
final_img.save("multiply.png", "PNG")

