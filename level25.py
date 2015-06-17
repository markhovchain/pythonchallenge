__author__ = 'dracz'

url25 = "http://www.pythonchallenge.com/pc/hex/lake.html"

# picture of a lake as a completed jigsaw puzzle in lake1.jpg
# puzzle is 5x5 = 25 pieces
# clue: 'can you see the waves?'
# title: 'imagine how they sound'

# looking for a wav file? there is not lake2.jpg
# but there is lake1.wav, lake2.wav, ..., lake25.wav
# on for each puzzle piece

import wave

from urlhelp import openurl

# all the audio files have:
# nframes: 10800
# framerate: 9600

# stitching them together and messing with the framerate doe not produce any decipherable sound
# maybe the bytes encode something else?
# if it encodes an image then there should be 3 bytes per pixel for rgb
# 10800/3 = 3600, maybe then each image file is a 60x60 pixel rgb image?

from PIL import Image, ImageShow
img = Image.new("RGB", (300, 300))

for i in range(0, 25):
    with openurl("http://www.pythonchallenge.com/pc/hex/lake{}.wav".format(i+1), "butter", "fly") as f:
        w = wave.open(f, "rb")
        piece = Image.frombytes("RGB", (60, 60), w.readframes(w.getnframes()))
        img.paste(piece, (60*(i % 5), 60*(i//5)))

ImageShow.show(img)

img.save("img/lake.png")

# it says: decent

url26 = "http://www.pythonchallenge.com/pc/hex/decent.html"

import prompt
prompt.openurl(url26)