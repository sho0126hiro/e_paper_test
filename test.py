#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in9b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import RPi.GPIO as GPIO
# init\


epd = epd2in9b.EPD()
epd.init()
print("clear")
epd.Clear(0xFF)

# # Drawing on the Horizontal image
# # ベタ画像（ピクセル情報のみ持つ画像データ）
# # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
# # https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes
HBlackimage = Image.new('1', (epd2in9b.EPD_HEIGHT, epd2in9b.EPD_WIDTH), 255)  # 298*126
HRedimage = Image.new('1', (epd2in9b.EPD_HEIGHT, epd2in9b.EPD_WIDTH), 255)  # 298*126    
# # create Draw Object
drawblack = ImageDraw.Draw(HBlackimage)
drawred = ImageDraw.Draw(HRedimage)
# # https://note.nkmk.me/python-pillow-imagedraw/

font24 = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc', 20)
drawblack.text((10, 0), 'hello\n日本語\nにほんご\nニホンゴ', font = font24, fill = 0)
drawred.text((150, 0), 'hello\n日本語\nにほんご\nニホンゴ', font = font24, fill = 0)
epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
time.sleep(1)
print("read bmp file")
blackimage1 = Image.new('1', (epd2in9b.EPD_HEIGHT, epd2in9b.EPD_WIDTH), 255)  # 298*126
newimage = Image.open('thinking_face.bmp')
blackimage1.paste(newimage, (0,0))    
# HBlackimage = Image.open('thinking_face.bmp')
epd.display(epd.getbuffer(blackimage1), epd.getbuffer(HRedimage))

epd.sleep()

# GPIO.cleanup()