from PIL import Image, ImageChops, ImageFilter 
from matplotlib import pyplot as plt

img = Image.open("./images/o.png")
img1 = Image.open("./images/x.png")

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

# convert colour mode:
gray = merged.convert('L')
gray.show()

# convert colour mode:
binary = merged.convert('1')
binary.show()

pixel = merged.load()

for row in range(merged.size[0]):
    for column in range(merged.size[1]):
        if pixel[row, column] != (255,255,255):
            pixel[row,column] = (255,0,0)
merged.show()