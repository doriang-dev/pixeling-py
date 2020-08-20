from PIL import Image


def hexify(rgb_color):
    hex_color = '#'
    for color in rgb_color:
        hex_component = hex(color)[2:]

        if color < 16:
            hex_color += '0'

        hex_color += hex_component

    return hex_color


def is_bw(rgb):
    somme = sum(rgb)
    if 120 <= somme <= 650:
        return False
    else:
        return True


def open_image(path, reducer):
    img = Image.open(path)

    width, height = img.size

    img.thumbnail((width * reducer, height * reducer))

    return img
