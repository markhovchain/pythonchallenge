__author__ = 'dracz'

url30 = "http://www.pythonchallenge.com/pc/ring/yankeedoodle.html"

# title: relax you are on 30
# hint: The picture is only meant to help you relax
# <!-- while you look at the csv file -->

# look for yankeedoodle.csv

def save_csv():
    from urlhelp import openurl
    with openurl("http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv", "repeat", "switch") as rf:
        with open("img/yankeedoodle.csv", "wb") as wf:
            wf.write(rf.read())

def read_csv():
    with open("img/yankeedoodle.csv", "rb") as f:
        return f.read()

def get_data(asints=True):
    csv = read_csv().decode()
    bb = [float(n) for n in csv.replace('\n', ' ').replace(' ', '').split(',')]
    if asints:
        return [round(255*n) for n in bb]
    return bb

import matplotlib.pyplot as plt

def plot_points(a):
    plt.plot(a)
    plt.show()

def plot_hist(a):
    plt.hist(a)
    plt.show()

def print_stats(a):
    from scipy import stats
    s = stats.describe(a)
    for n in ["nobs", "minmax", "mean", "variance", "skewness", "kurtosis"]:
        print("{:<10} {}".format(n+":", getattr(s, n)))

"""
nobs:      7367
minmax:    (0.12154, 0.99997999999999998)
mean:      0.7349867924528303
variance:  0.0366251383482359
skewness:  -0.8266960187328959
kurtosis:  -0.19682819894251757
"""

# odd number of observations -> not rectangular

# does relax imply relaxed parsing? or rounding?
# does "look at the csv file" mean visualize as plot of image?

from PIL import Image, ImageShow
import prompt


def get_dims(length=7367):
    # find the image dimensions that fit the data
    return [(w, h) for w in range(32, 320) for h in range(32, 320) if w*h == length]

# the only dimensions that work for length=7367 are (53, 139) and (139, 53)
# the first one actully shows something

def show_image(dims=(53, 139)):
    w, h = dims
    img = Image.frombytes("P", (w, h), bytes(get_data()))
    # when we view the image, it is rotated
    img = img.transpose(Image.ROTATE_270)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.show()
