from PIL import Image, ImageChops, ImageFilter 
from matplotlib import pyplot as plt

img = Image.open("./images/yahre1.jpg")
img1 = Image.open("./images/liam1.jpg")

img.show()
img1.show()
print("image size: ", img.size, "colour mode: ", img._mode)
print("image size 1: ", img1.size, "colour mode: ", img1._mode)

plt.subplot(121), plt.imshow(img)
plt.axis('off')
plt.subplot(122), plt.imshow(img1)
plt.axis('off')

# multilpy images:
merged = ImageChops.multiply(img, img1)
merged.show()

add = ImageChops.add(img, img1)
add.show()