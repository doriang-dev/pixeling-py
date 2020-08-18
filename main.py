from time import time

from utils.img_tools import get_pixels, open_image


def main_color(img_path):
    ti = time()
    img = open_image(img_path)
    pixels = get_pixels(img)
    # count = counter(pixels)
    # sorted_count = sorted(count.items(), key=lambda value: value[1], reverse=True)

    print(pixels)
    # print(sorted_count[0:10])
    tf = time()
    print('temps:', tf - ti)


if __name__ == '__main__':
    FILES = ['imgtest/index.jpg', 'imgtest/test.jpg']
    for file in FILES:
        print('\n', file)
        main_color(file)
