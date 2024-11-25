import easyocr
import time

reader = easyocr.Reader(['ch_sim', 'en'])
read_img = reader.readtext("price.png")
for i in read_img:
    world = i[1]
    print(world)