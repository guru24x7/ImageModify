from PIL import Image
box = (100, 100, 400, 400)
im = Image.open("19.jpg")
region = im.crop(box)

region = region.transpose(Image.ROTATE_90)
im.paste(region, box)
im.show()
