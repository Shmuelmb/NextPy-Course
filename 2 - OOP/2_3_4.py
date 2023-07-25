class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._color = (red, green, blue)

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average_colors = int(sum(self._color) // 3)
        self._color = (average_colors, average_colors, average_colors)

    def print_pixel_info(self):
        color_non_zero = ''
        colors = ["Red", "Green", "Blue"]
        if self._color.count(0) == 2:
            color_non_zero = colors[self._color.index(max(self._color))]
        print(
            f"X: {self._x}, Y: {self._y}, Color: {self._color} {color_non_zero}")


def main():

    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == "__main__":
    main()
