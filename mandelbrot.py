__author__ = 'dracz'


def mandelbrot(w, h, max_iter=128, x0=-2, x1=0.5, y0=-1.25, y1=1.25):
    """
    Generate mandelbrot set with specified width, height
    Using specified max iterations and domain of computation.
    Returns list of list of integer escape time values
    """
    rows = []
    dx = x1 - x0
    dy = y1 - y0
    for j in range(h):
        row = []
        for i in range(w):
            x = x0 + dx*i/w
            y = y0 + dy*j/h
            z = 0 + 0j
            c = x + 1j*y
            esc = max_iter-1  # the escape time default
            for n in range(max_iter):
                z = z**2 + c
                if abs(z) > 2:
                    esc = n
                    break
            row.append(esc)
        rows.append(row)
    return rows


from PIL import Image

def render(w, h, max_iter=128, x0=-2, x1=0.5, y0=-1.25, y1=1.25):
    """ Generate and render an image of a mandelbrot set over the specified domain.
    Returns an Image in palette mode with pixel value set to
    the escape time value for the pixel
    """
    img = Image.new("P", (w, h))
    for y, row in enumerate(mandelbrot(w, h, max_iter, x0, x1, y0, y1)):
        for x, v in enumerate(row):
            img.putpixel((x, y), v)
    return img.transpose(Image.FLIP_TOP_BOTTOM)

