from PIL import Image, ImageChops, ImageFilter 

img = Image.open("./images/yahre1.jpg")

img.show()
print("image size: ", img.size, "colour mode: ", img._mode)
