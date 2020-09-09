from PIL import Image
from utils.img_tools import *
from utils.contrast import *


class ColorGenerator:
    def __init__(self):
        self.__img = None
        self.__contrast_min = 0
        self.__pixels = []
        self.__scheme = []

    # Getters
    def __getsize__(self):
        return self.__img.size

    def __getpixels__(self):
        return self.__pixels

    def __getcontrast__(self):
        return self.__contrast_min

    # Setters
    def open(self, path):
        self.__img = Image.open(path)

        return True

    def reduce(self, size):
        self.__img.thumbnail((size, size))

        return size, size

    def set_pixeling(self, percentage):
        width, height = self.__getsize__()
        step = int(100 / percentage)

        for x in range(0, width, step):
            for y in range(height):
                pixel = self.__img.getpixel((x, y))

                self.__pixels.append(pixel)

        return len(self.__pixels)

    def scheme(self, length, reduce=False):
        reducer = 200 if reduce else 500

        self.reduce(reducer)
        self.set_pixeling(75)

        self.__contrast_min = 21 / (length * 3)

        for pixel in self.__pixels:
            if is_bw(pixel):
                continue

            if not self.__scheme:
                self.__scheme.append(pixel)
                continue

            add = True
            for color in self.__scheme:
                c = contrast(pixel, color)
                if c <= self.__contrast_min:
                    add = False
                    break

            if add:
                self.__scheme.append(pixel)

        return self.__scheme
