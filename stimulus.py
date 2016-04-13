import numpy

def circle(n, radius, solid=False, center=None, width=1):
    """Make an `n` by `n` array with a circle of radius `radius`.
    Ignores width if solid is true.
    Defaults to centering in the middle, and width 1"""
    canvas = numpy.zeros((n, n))
    num = n - 1  # the number of rows
    x, y = (num / 2.0, num / 2.0) if center is None else center
    if solid:
        fill = lambda i, j: ((x - j) ** 2 + (y - i) ** 2) ** .5 <= radius
    else:
        fill = lambda i, j: radius - width <= ((x - j) ** 2 + (y - i) ** 2) ** .5 <= radius + width
    for i, row in enumerate(canvas):
        for j, pt in enumerate(row):
            if fill(i, j):
                canvas[i, j] = 1.0
    return canvas

