from PIL import Image

img = Image.open("josevicente.jpeg")
pixels = img.load()  # acceso directo a píxeles

width, height = img.size

for y in range(height):
    for x in range(width):
        pixel = pixels[x, y]
        print(x, y, pixel)
