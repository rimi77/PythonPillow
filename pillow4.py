from PIL import Image, ImageFilter

# Open an image file
img = Image.open("./images/liam1.jpg")

# Display the image
img.show()

# Image Blending:
# Open another image
img2 = Image.open("./images/yahre1.jpg")

# Blend the images
blended_img = Image.blend(img, img2, alpha=0.7)

# Display the blended image
blended_img.show()