import glob

from src.pixel_map import PixelMap
from PIL import Image

DEFAULT_DIMENSIONS = 32

COLOUR_TYPE = 'RGB'

class Trainer():
    def __init__(self, name, size_x=DEFAULT_DIMENSIONS, size_y=DEFAULT_DIMENSIONS):
        print 'creating new trainer...'
        self.name           = name
        self.size_x         = size_x
        self.size_y         = size_y
        self.colour_type    = COLOUR_TYPE

        self.pixels = []
        for i in range(self.size_x):
            self.pixels.append([])
            for j in range(self.size_y):
                self.pixels[i].append(PixelMap())

    def train_images(self, path):
        print 'starting training...'
        for filename in glob.glob(path):
            print filename
            image = Image.open(filename).convert(self.colour_type)

            for i in range(self.size_x):
                for j in range(self.size_y):
                    self._train_pixel(i, j, image)
        self.calculate()

    def _train_pixel(self, x, y, image):
        self.pixels[x][y].add_entry(x, y, image)

    def calculate(self):
        print 'starting calculations...'
        for i in range(self.size_x):
            print str(i)+'...'
            for j in range(self.size_y):
                self.pixels[i][j].calculate()


    def display(self):
        self.pixels[8][8].display()
