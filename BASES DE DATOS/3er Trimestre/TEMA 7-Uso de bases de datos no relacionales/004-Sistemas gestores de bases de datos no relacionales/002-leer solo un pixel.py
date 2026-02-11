from PIL import Image

img = Image.open("gatoo boom.jpg")
pixels = img.load()  # acceso directo a píxeles

pixel = pixels[0,0]
print(pixel)

