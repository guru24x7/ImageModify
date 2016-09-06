from PIL import Image
im = Image.open("19.jpg")

print(im.format, im.size, im.mode)
im.show()
