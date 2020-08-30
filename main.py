from time import time

from utils.colors_generator import generate_color_scheme
from utils.img_tools import hexify
from colr import color

CONTRAST = 1.5
FORE = 'ffffff'
COLOR_SCHEME_LENGTH = 10


def main(path):
    ti = time()

    color_scheme = generate_color_scheme(path, COLOR_SCHEME_LENGTH, CONTRAST)

    for color_pixel in color_scheme:
        hex_color = hexify(color_pixel)

        print(color(hex_color, fore=FORE, back=color_pixel))

    tf = time()

    print('temps: ' + str(tf - ti))
    print('longueur: ' + str(len(color_scheme)))


if __name__ == '__main__': # TODO: Enter file in CLI command (not with input() function)
    # FILES = ('desert', 'index', 'lac', 'test', 'test2')
    # for filename in FILES:
    #     path = 'imgtest/' + filename + '.jpg'
    #     print('\n' + path)
    #     main(path)

    filename = input('img name: ')
    main('imgtest/' + filename + '.jpg')
