def light_tool(value):
    value = value / 255
    return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    a = list(map(light_tool, rgb))
    return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722


def contrast(color1, color2):
    lum1 = luminance(color1)
    lum2 = luminance(color2)
    lightest = max(lum1, lum2)
    darkest = min(lum1, lum2)

    return (lightest + 0.05) / (darkest + 0.05)
