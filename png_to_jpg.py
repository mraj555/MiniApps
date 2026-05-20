from PIL import Image

img = Image.open("image.png")
jpeg_img = img.convert("RGB")

jpeg_img.save("converted.jpeg")
