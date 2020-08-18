from PIL import Image


def hexify(rgb_color):
    hex_color = 'h'
    for color in rgb_color:
        hex_color += hex(color)[2:]

    return hex_color


def open_image(path):  # TODO: test if the thumbnail is a good solution
    size = 4, 4
    img = Image.open(path)
    img.thumbnail(size)

    return img


def get_pixels(image):
    width, height = image.size
    pixels = []

    for i in range(height):
        for j in range(width):
            pixel = image.getpixel((i, j))
            somme = 0

            for color in pixel:
                somme += color

            if 100 <= somme <= 700:
                pixels += [hexify(pixel)]

    return pixels
