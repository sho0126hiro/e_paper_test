from PIL import Image

img = Image.open('thinking_face.bmp')
r = img.resize((30,30))
img.save('thinking_face30.bmp')