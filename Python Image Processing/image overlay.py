from PIL import Image
import numpy as np
import cv2

img1 = Image.open('/Users/emily/PycharmProjects/ImageProcessingTest/(1,3)/CD31_darkred.jpg')
imgrgba1 = img1.convert("RGBA")
img2 = Image.open('/Users/emily/PycharmProjects/ImageProcessingTest/(1,3)/pimo_green.jpg')
imgrgba2 = img2.convert("RGBA")
img3 = Image.open('/Users/emily/PycharmProjects/ImageProcessingTest/(1,3)/carbo_lightblue.jpg')
imgrgba3 = img3.convert("RGBA")


# adds a sepia hue
def add_hue(image):
    im_color = cv2.applyColorMap(image, cv2.COLORMAP_OCEAN)
    img_color = Image.fromarray(im_color)
    return img_color


arr = np.array(img1)
imgcolor1 = add_hue(arr)
imgcolor1.show()

# alpha compositing images:
alpha_one = Image.alpha_composite(imgrgba1, imgrgba2)
alpha_one.show()

alpha_two = Image.alpha_composite(alpha_one, imgrgba3)
alpha_two.show()
alpha_two.save('composite_img.png', 'PNG')

