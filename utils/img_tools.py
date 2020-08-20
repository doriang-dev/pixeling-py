from math import sqrt
from utils.contrast import contrast

from PIL import Image
from colr import color


def hexify(rgb_color):
    hex_color = '#'
    for color in rgb_color:
        hex_component = hex(color)[2:]

        if color <= 15:
            hex_color += '0'

        hex_color += hex_component

    return hex_color


def is_bw(rgb):
    somme = sum(rgb)
    if 100 <= somme <= 700:
        return False
    else:
        return True


def open_image(path):
    return Image.open(path)


def generatecolorscheme(path, nb_colors):
    img = open_image(path)

    width, height = img.size

    size = width

    img.thumbnail((size, size))

    # step = int(size / nb_colors)

    pixels = []

    for x in range(0, size, nb_colors):
        for y in range(0, size, nb_colors):

            pixel = img.getpixel((x, y))

            if is_bw(pixel):
                break

            if len(pixels) == 0:
                pixels.append(pixel)

            else:  # TODO: contrast par rapport à toutes les couleurs de la liste
                last = len(pixels) - 1
                last_pixel = pixels[last]
                contrast_color = contrast(pixel, last_pixel)

                if contrast_color >= 3:
                    pixels.append(pixel)

    return pixels
