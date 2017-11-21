from src.pixel_info import PixelInfo
NEIGHBOUR_DEPTH = 1

DEFAULT_VALUE = (0, 0, 0)

class PixelMap():

    def __init__(self, neighbour_depth_x=NEIGHBOUR_DEPTH, neighbour_depth_y=NEIGHBOUR_DEPTH):
        self.neighbour_depth_x = neighbour_depth_x
        self.neighbour_depth_y = neighbour_depth_y

        self.neighbours = {}
        for i in range(-1 * self.neighbour_depth_x, self.neighbour_depth_x + 1):
            for j in range(-1 * self.neighbour_depth_y, self.neighbour_depth_y + 1):
                self.neighbours[(i,j)] = PixelInfo()

    def display(self):
        for i in range(-1 * self.neighbour_depth_x, self.neighbour_depth_x + 1):
            rows = []
            for j in range(-1 * self.neighbour_depth_y, self.neighbour_depth_y + 1):
                rows.append(self.neighbours[(i,j)])
            print rows


    def add_entry(self, x, y, image):
        for i in range(-1 * self.neighbour_depth_x, self.neighbour_depth_x + 1):
            for j in range(-1 * self.neighbour_depth_y, self.neighbour_depth_y + 1):
                # TODO upper bound checks instead of try/catch
                if (x+i >= 0) and (y+j >= 0):
                    try:
                        self.neighbours[(i,j)].add_entry(image.getpixel((x+i,y+j)))
                    except IndexError:
                        self.neighbours[(i,j)].add_entry(DEFAULT_VALUE)

    def calculate(self):
        for i in range(-1 * self.neighbour_depth_x, self.neighbour_depth_x + 1):
            for j in range(-1 * self.neighbour_depth_y, self.neighbour_depth_y + 1):
                self.neighbours[(i,j)].calculate()
