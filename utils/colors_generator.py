from utils.contrast import contrast
from utils.img_tools import open_image, is_bw


def generate_color_scheme(path, nb_colors, contrasting):
    reducer = 0.5 + (nb_colors / 50)
    # reducer = 1
    img = open_image(path, reducer)

    size, height = img.size

    step = int(size / nb_colors)

    pixels = []

    for x in range(0, size, step):
        for y in range(0, height, step):

            pixel = img.getpixel((x, y))

            if is_bw(pixel):
                continue

            if len(pixels) == 0:
                pixels.append(pixel)

            else:
                add = True
                for color in pixels:
                    if contrast(pixel, color) <= contrasting:
                        add = False
                        break

                if add:
                    pixels.append(pixel)

    print('size: ' + str(size) + 'px')
    print('Contrast: ' + str(contrasting))
    print('Length: ' + str(nb_colors))
    print('Reducer: ' + str(reducer))
    return pixels[:nb_colors]