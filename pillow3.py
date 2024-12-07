from PIL import Image, ImageFilter

# Open an image file
img = Image.open("./images/family.JPG")

# Display the image
img.show()

# Apply a blur filter
#blurred_img = img.filter(ImageFilter.BLUR)
blurred_img = img.filter(ImageFilter.GaussianBlur(15))

# Display the blurred image
blurred_img.show()