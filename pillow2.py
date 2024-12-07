from PIL import Image

# Open an image file
img = Image.open("./images/danza1.jpg")

# Display the image
img.show()

# Image Properties
print(img.format) # Output: JPEG
print(img.size) #Output: (600,800)
print(img.mode) # Output: RGB

# Crop the image (recortar)
cropped_img = img.crop((100, 200, 400, 500))

# Resize the image
resized_img = img.resize((300, 400))

# Display the cropped and resized images
cropped_img.show()
resized_img.show()

# Saving an Image
cropped_img.save("dancer_cropped.jpg")
resized_img.save("dancer_resized.png")

