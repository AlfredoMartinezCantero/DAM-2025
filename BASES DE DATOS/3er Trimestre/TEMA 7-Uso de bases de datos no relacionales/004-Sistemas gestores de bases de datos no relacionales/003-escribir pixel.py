from PIL import Image

# Abrir imagen original
img = Image.open("gatoo boom.jpg")
pixels = img.load()

# Leer el color del píxel (0,0)
pixel_color = pixels[0, 0]
print(pixel_color)

# Crear una nueva imagen (por ejemplo 100x100)
new_img = Image.new(img.mode, (100, 100))
new_pixels = new_img.load()

new_pixels[0, 0] = (255,0,0)

new_img.save("guardado.png")

