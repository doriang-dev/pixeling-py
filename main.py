from utils.img_tools import hexify
from utils.Generator import ColorGenerator
from colr import color as term_color

colors = ColorGenerator()
colors.open('imgtest/lac.jpg')
scheme = colors.scheme(length=6)

list(map(hexify, scheme))

for color in scheme:
    print(term_color(color, fore='fff', back=color))

print(colors.__getcontrast__())

