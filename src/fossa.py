from PIL import Image
import glob
import random

from trainer import Trainer
from piece import Piece
from pixel_map import PixelMap

#TODO restrict filetypes

class Fossa():
    def __init__(self):
        self.trainers = {}

        #self.create_new_trainer('Tester', 32, 32)
        #self.train('Tester', 'images/')
        #self.create_random_pixel_piece('Tester')

        self.create_new_trainer('water', 250, 250)
        self.train('water', 'images/water/')
        self.create_random_pixel_piece('water')

    def create_new_trainer(self, name, size_x, size_y):
        self.trainers[name] = Trainer(name, size_x, size_y)

    def train(self, trainer_name, image_directory):
        path = image_directory + '*' 
        self.trainers[trainer_name].train_images(path)

    def create_random_pixel_piece(self, trainer_name):
        trainer = self.trainers[trainer_name]

        for i in range(1):
            im = Image.new(trainer.colour_type, (trainer.size_x, trainer.size_y), "black")
            pixels = im.load()

            for j in range(self.trainers[trainer_name].size_x):
                for k in range(self.trainers[trainer_name].size_y):
                    r1 = (0,0)
                    value = trainer.pixels[j][k].neighbours[r1].mean
                    std = trainer.pixels[j][k].neighbours[r1].stdd
                    #pixels[j, k] = random.choice(trainer.pixels[j][k].neighbours[(0,0)].entries.keys())
                    pixels[j, k] = (value[0], value[1], value[2])

            im.save('renders/test'+str(i)+'.png')
            del im

        print 'done'
