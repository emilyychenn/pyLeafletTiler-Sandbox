# import blend_modes # used for image compositing below
from PIL import Image
import numpy as np
import cv2


# adds a sepia hue
def add_hue(image):
    im_color = cv2.applyColorMap(image, cv2.COLORMAP_OCEAN)
    img_color = Image.fromarray(im_color)
    return img_color


im_gray1 = cv2.imread("./(1,3)/CD31_darkred.jpg", cv2.IMREAD_GRAYSCALE)
imgwithhue = add_hue(im_gray1)

im_gray2 = cv2.imread("./(1,3)/pimo_green.jpg", cv2.IMREAD_GRAYSCALE)
imgwithhue2 = add_hue(im_gray2)
imgwithhue2.save("oceancolormap.png", "PNG")

im_gray3 = cv2.imread("./(1,3)/carbo_lightblue.jpg", cv2.IMREAD_GRAYSCALE)
imgwithhue3 = add_hue(im_gray3)


# shifts hue to red, green or blue
def shift_hue(arr, hout):
    rgb = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB) # OpenCV reads the images as BRG instead of RGB
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    hsv[...,0] = hout
    rgb2 = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    return rgb2


arr = np.array(imgwithhue)
arr2 = np.array(imgwithhue2)
arr3 = np.array(imgwithhue3)


if __name__=='__main__':
    green_hue = 60
    red_hue = 0
    blue_hue = 90

    colored_img1 = Image.fromarray(shift_hue(arr, red_hue))
    colored_img1.save('image1_red.jpg') # saved as jpg for the jupyter notebook (for tile generation)

    colored_img2 = Image.fromarray(shift_hue(arr2, green_hue))
    colored_img2.save('image2_green.jpg')

    colored_img3 = Image.fromarray(shift_hue(arr3, blue_hue))
    colored_img3.save('image3_blue.jpg')


# code for image compositing; in case two layers need to be flattened/composited before uploading to leaflet
# uncomment to use

# imgrgba1 = colored_img1.convert("RGBA")
# img1arr = np.array(imgrgba1)
# image1_float = img1arr.astype(float)  # Inputs to blend_modes need to be floats
#
# imgrgba2 = colored_img2.convert("RGBA")
# img2arr = np.array(imgrgba2)
# image2_float = img2arr.astype(float)  # Inputs to blend_modes need to be floats
#
# imgrgba3 = colored_img3.convert("RGBA")
# img3arr = np.array(imgrgba3)
# image3_float = img3arr.astype(float)  # Inputs to blend_modes need to be floats
#
# multiply_img = blend_modes.multiply(image1_float, image2_float, 1)
# multiply2_img = blend_modes.multiply(multiply_img, image3_float, 1)
# uint8_img = np.uint8(multiply2_img) # Image needs to be converted back to uint8 type for PIL handling.
# final_img = Image.fromarray(uint8_img)
# final_img.show()
# final_img.save("multiply.png", "PNG")


# Note: final image must be overlaid onto a background with dimensions proportional to tile size
# this ensures tiles are exactly squares so that no stretching occurs!
