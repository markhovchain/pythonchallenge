__author__ = 'dracz'

from urlhelp import openurl

url19 = 'http://www.pythonchallenge.com/pc/hex/bin.html'

html = openurl(url19, 'butter', 'fly').read().decode()

# title: please!
# in page comments: there is an email msg with base64 encoded wav file:

"""
From: leopold.moz@pythonchallenge.com
Subject: what do you mean by "open the attachment?"
Mime-version: 1.0
Content-type: Multipart/mixed; boundary="===============1295515792=="

It is so much easier for you, youngsters.
Maybe my computer is out of order.
I have a real work to do and I must know what's inside!


Content-type: audio/x-wav; name="indian.wav"
Content-transfer-encoding: base64

UklGRvyzAQBXQVZFZm10IBAAAAABAAEAESsA ...
"""

# let's extract and decode the wav file, then listen to it

import base64
import re

b64 = re.search(r'base64\n\n(.*)\n\n--=====', html, re.S).group(1).replace('\n', '')

indian = "img/indian.wav"

with open(indian, "wb") as f:
    print("writing {}...".format(f.name))
    f.write(base64.b64decode(b64.encode()))

# file contains fuzzy clip that says: "sorry!"
# visiting sorry.html -> - "what are you apologizing for?"

# perhaps there are multiple audio files interleaved, like in earlier images?

import wave

with wave.open(indian) as f:
    frames = f.readframes(f.getnframes())
    for i in range(2):
        name = "img/indian{}.wav".format(i+1)
        with wave.open(name, "wb") as fn:
            print("writing {}...".format(name))
            fn.setnchannels(f.getnchannels())
            fn.setsampwidth(f.getsampwidth())
            fn.setframerate(f.getframerate()//2)
            fn.setnframes(f.getnframes())
            fn.writeframes(frames[i::2])


# the first wav says: "you are an idiot, ha ha-ha ha-ha-ha-ha!
# the second says more clearly: "sorry!"

url20 = 'http://www.pythonchallenge.com/pc/hex/idiot.html'

import prompt
prompt.openurl(url20, 20)

# picture of leopold: "now you should apologize..."
# like to actual level: 'http://www.pythonchallenge.com/pc/hex/idiot2.html'

url20 = 'http://www.pythonchallenge.com/pc/hex/idiot2.html'
prompt.openurl(url20, 20)
