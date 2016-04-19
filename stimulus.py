import numpy
import math


def zeros(n):

    return numpy.zeros((n, n))

def circle(n, radius, solid=False, center=None, width=1, norm=False):
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
    if norm:
        return canvas/numpy.sum(canvas)
    else:
        return canvas


def rotating_bar(size, n_frames, rads_per_frame, width=1, angle=0, norm=False):

    for f in range(n_frames):
        canvas = numpy.zeros((size, size))
        a, b = math.cos(angle), math.sin(angle)
        for i, row in enumerate(canvas):
            for j, pt in enumerate(row):
                if abs(a * (i-size/2) + b * (j-size/2)) <= width/2.0:
                    canvas[i, j] = 1.0
        if norm:
            yield canvas/numpy.sum(canvas)
        else:
            yield canvas
        angle += rads_per_frame
