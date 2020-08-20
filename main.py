from utils.img_tools import generatecolorscheme, hexify
from colr import color


def main():
    # path = input('img path: ')
    path = 'imgtest/index.jpg'
    color_scheme = generatecolorscheme(path, 5)

    for color_pixel in color_scheme:
        hex_color = hexify(color_pixel)
        print(color(hex_color, fore='ffffff', back=color_pixel))


if __name__ == '__main__':
    main()
