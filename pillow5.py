from PIL import Image, ImageFilter

# Open an image file
#img = Image.open("./images/figurasColores.png")
img = Image.open("./images/danza3.jpg")

# Display the image
img.show()

# Rotating and Flipping:
# Rotate the image by 45 degrees
rotated_img = img.rotate(45)

# Flip the image vertically
flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)

# Display the rotated and flipped images
rotated_img.show()
flipped_img.show()