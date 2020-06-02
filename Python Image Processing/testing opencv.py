from PIL import Image
import numpy as np
import cv2


# adds a slight sepia hue
def add_hue(image):
    im_color = cv2.applyColorMap(image, cv2.COLORMAP_OCEAN)
    img_color = Image.fromarray(im_color)
    return img_color


im_gray1 = cv2.imread("./(1,5)/CD31(1,5).jpg", cv2.IMREAD_GRAYSCALE)
imgwithhue = add_hue(im_gray1)

im_gray2 = cv2.imread("./(1,5)/pimo(1,5).jpg", cv2.IMREAD_GRAYSCALE)
imgwithhue2 = add_hue(im_gray2)

im_gray3 = cv2.imread("./(1,5)/carbo(1,5).jpg", cv2.IMREAD_GRAYSCALE)
imgwithhue3 = add_hue(im_gray3)


# shifts hue to red, green or blue
def shift_hue(arr, hout):
    rgb = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB) #OpenCV reads the images as BRG instead of RGB
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

    new_img = Image.fromarray(shift_hue(arr, red_hue))
    new_img.save('image1_red.png')

    new_img2 = Image.fromarray(shift_hue(arr2, green_hue))
    new_img2.save('image2_green.png')

    new_img3 = Image.fromarray(shift_hue(arr3, blue_hue))
    new_img3.save('image3_blue.png')


# to make white pixels in image transparent
def transparency(image):
    imgrgba = image.convert("RGBA")

    datas1 = imgrgba.getdata()
    newData1 = []
    for item in datas1:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData1.append((255, 255, 255, 0))
        else:
            newData1.append(item)
    imgrgba.putdata(newData1)

    imgarr = np.array(image)
    greyarr = np.sum(imgarr, axis=2)

    # thresholded approach, select all pixels above certain intensity
    index = greyarr >= 3 * 254
    transparency_layer = 255 * np.ones_like(imgarr[:, :, 0])
    transparency_layer[index] = 0

    # alternative
    transparency_layer = (255 - greyarr // 3).astype(np.uint8)

    # set alpha channel
    imgrgba.putalpha(Image.fromarray(transparency_layer))

    return imgrgba


img = Image.open("image1_red.png")
imgrgba = transparency(img)
imgrgba.save('layer1.png', 'PNG')
processed_layer1 = Image.open("layer1.png")

img2 = Image.open("image2_green.png")
img2rgba = transparency(img2)
img2rgba.save('layer2.png', 'PNG')
processed_layer2 = Image.open("layer2.png")

img3 = Image.open("image3_blue.png")
img3rgba = transparency(img3)
img3rgba.save('layer3.png', 'PNG')
processed_layer3 = Image.open("layer3.png")


# create background layer (white):
background = Image.new('RGBA', img.size, "white")
pixels = background.load()


# overlay images:
alpha_one = Image.alpha_composite(processed_layer2, processed_layer1)

alpha_two = Image.alpha_composite(alpha_one, processed_layer3)

alpha_three = Image.alpha_composite(background, alpha_two)
alpha_three.show()
alpha_three.save('composite_img.png', 'PNG')

# working image blend:
img_blend = Image.blend(processed_layer1, processed_layer2, 0.5)
# img_blend2 = Image.blend(img_blend, processed_layer3, 0.5)
alpha_blend = Image.alpha_composite(img_blend, processed_layer3)

# img_blend2.putalpha(255)

alpha_final = Image.alpha_composite(background, alpha_blend)
alpha_final.show()
alpha_final.save('blended_img.png', 'PNG')
