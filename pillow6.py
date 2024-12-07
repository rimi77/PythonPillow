from PIL import Image

filename_cat = "./images/gato.jpg"

with Image.open(filename_cat) as img_cat:
    img_cat.load()
img_cat = img_cat.crop((800, 0, 1650, 1281))
img_cat.show()

img_cat_gray = img_cat.convert("L")
img_cat_gray.show()
threshold = 100
img_cat_threshold = img_cat_gray.point(
     lambda x: 255 if x > threshold else 0
)
img_cat_threshold.show()

red, green, blue = img_cat.split()
red.show()
green.show()
blue.show()

threshold = 57
img_cat_threshold = blue.point(lambda x: 255 if x > threshold else 0)
img_cat_threshold = img_cat_threshold.convert("1")
img_cat_threshold.show()
